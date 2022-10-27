#!/usr/bin/env python3
#
# Copyright (c) 2022 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
#
# Download and install the amdfwflash utility
# V0.3: exit on amdgpu driver
# V0.2: fix ubuntu
# V0.1: Initial version 10.26.2022
#
from urllib import request
from urllib.request import urlretrieve
import re
import subprocess
import sys
import argparse
import os
import shlex
import datetime

# Set ROCm Release Package Distribution repo baseURL below
fwupdatorurl = { "1.0" :
        { "sles" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm",
        "centos8" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm",
        "rhel8" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm",
        "centos9" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm",
        "rhel9" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm",
        "ubuntu" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/deb",
        "centos" : "https://repo.radeon.com/fwupdator/amdfwflash/.1.0/rpm"
        }
    }

# Commands
RM_F_CMD = "/bin/rm -f "
RPM_CMD = "/usr/bin/rpm"
YUM_CMD = "/usr/bin/yum"
DPKG_CMD = "/usr/bin/dpkg"
DPKGDEB_CMD = "/usr/bin/dpkg-deb"
APTGET_CMD = "/usr/bin/apt-get"
APT_CMD = "/usr/bin/apt"
APTKEY_CMD = "/usr/bin/apt-key"
WGET_CMD = "/usr/bin/wget"
ZYPPER_CMD = "/usr/bin/zypper"
ECHO_CMD = "/bin/echo"
TEE_CMD = "/usr/bin/tee"
LSMOD_CMD = "/sbin/lsmod"
GREP_CMD = "/bin/grep"
AMDFWFLASH_CMD = "/opt/amdfwflash/bin/amdfwflash"
SED_CMD = "/bin/sed"

# Package type suffixes
PKGTYPE_RPM = "rpm"
PKGTYPE_DEB = "deb"

# Supported OS types
CENTOS_TYPE = "centos" # Version 7
CENTOS8_TYPE = "centos8"
CENTOS9_TYPE = "centos9"
UBUNTU_TYPE = "ubuntu"
DEBIAN_TYPE = "debian"
SLES_TYPE = "sles"
RHEL_TYPE = "rhel" # Version 7
RHEL8_TYPE = "rhel8"
RHEL9_TYPE = "rhel9"

CENTOS_VERSION8_TYPESTRING = 'VERSION="8'
CENTOS_VERSION9_TYPESTRING = 'VERSION="9'
RHEL_VERSION8_TYPESTRING = 'VERSION="8'
RHEL_VERSION9_TYPESTRING = 'VERSION="9'

BIONIC_TYPE = "bionic"
FOCAL_TYPE = "focal"
JAMMY_TYPE = "jammy"


# OS release info
ETC_OS_RELEASE = "/etc/os-release"
# Download destination dir: default current director
DOWNLOAD_DESTDIR = "./"

#
# Is amdgpu driver loaded?
#
def is_amdgpu_driver_loaded():
    check_cmd = LSMOD_CMD
    grep_cmd = GREP_CMD + " amdgpu "
    try:
        ps1 = subprocess.Popen(shlex.split(check_cmd), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        ps2 = subprocess.Popen(shlex.split(grep_cmd), stdin=ps1.stdout, stdout=subprocess.PIPE)
        ps1.stdout.close()
        out = ps2.communicate()[0]
        print(out.decode('utf-8'))
        if ps2.returncode == 0:
            return True
        else:
            return False
    except subprocess.CalledProcessError as err:
        return False

#
# Is iomem=relaxed set?
#
def is_iomem_relaxed_set():
    check_cmd = "cat /proc/cmdline"
    grep_cmd = GREP_CMD + " iomem=relax "
    try:
        ps1 = subprocess.Popen(shlex.split(check_cmd), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        ps2 = subprocess.Popen(shlex.split(grep_cmd), stdin=ps1.stdout, stdout=subprocess.PIPE)
        ps1.stdout.close()
        out = ps2.communicate()[0]
        print(out.decode('utf-8'))
        if ps2.returncode == 0:
            return True
        else:
            return False
    except subprocess.CalledProcessError as err:
        return False

# Remove iomem=relaxed parameter
def remove_iomem_relaxed_param():
    update_grub_cmd = "sed -i 's/ iomem=relaxed//' /etc/default/grub"
    try:
        ps1 = subprocess.Popen(shlex.split(update_grub_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
       for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
       return False

    grub2_mkconfig_cmd = "grub2-mkconfig -o /boot/grub2/grub.cfg"
    try:
        ps1 = subprocess.Popen(shlex.split(grub2_mkconfig_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
       for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
       return False
    return True

# update ifwi
def update_ifwi():
    update_cmd = AMDFWFLASH_CMD + " --update-ifwi"
    try:
        ps1 = subprocess.Popen(shlex.split(update_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
       for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
       return False
    return True

# rollback ifwi
def rollback_ifwi():
    rollback_cmd = AMDFWFLASH_CMD + " --rollback-ifwi"
    try:
        ps1 = subprocess.Popen(shlex.split(rollback_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
       for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
       return False
    return True

# list devices
def list_devices():
    listdev_cmd = AMDFWFLASH_CMD + " --list-devices"
    try:
        ps1 = subprocess.Popen(shlex.split(listdev_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
       for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
       return False
    return True

# Setup/remove repo
def setup_sles_zypp_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # Set up rocm repo for chosen rev to install
        # use rev specific rocm repo
        zypprepo = "[amdfwflash" + args.revstring[0] + "]\nenabled=1\nautorefresh=0\nbaseurl=" + fetchurl + "\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://repo.radeon.com/fwupdator/amdfw.gpg.key"
        echocmd = ECHO_CMD + " -e '" + zypprepo + "' "
        repofilename = "/etc/zypp/repos.d/amdfwflash" + args.revstring[0] + ".repo "
        teecmd = TEE_CMD + " " + repofilename + " "
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # apt update repo
        zypprefresh = ZYPPER_CMD + " refresh "
        try:
            ps1 = subprocess.Popen(zypprefresh.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_centos_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # Set up rocm repo for chosen rev to install
        # use rev specific rocm repo
        yumrepo = "[amdfwflash" + args.revstring[0] +"]\nname=amdfwflash\nbaseurl=" + fetchurl + "\nenabled=1\ngpgcheck=1\ngpgkey=https://repo.radeon.com/fwupdator/amdfw.gpg.key"
        echocmd = ECHO_CMD + " -e '" + yumrepo + "' "
        repofilename = "/etc/yum.repos.d/amdfwflash" + args.revstring[0] + ".repo"
        teecmd = TEE_CMD + " " + repofilename + " "
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # clean repo
        yumupdate = YUM_CMD + " clean all "
        try:
            ps1 = subprocess.Popen(yumupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_centos9_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        setup_centos_repo(args, fetchurl)

def setup_centos8_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        setup_centos_repo(args, fetchurl)

def remove_centos_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/yum.repos.d/amdfwflash" + args.revstring[0] + ".repo"
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        yumupdate = YUM_CMD + " clean all "
        try:
            ps1 = subprocess.Popen(yumupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def remove_sles_zypp_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/zypp/repos.d/amdfwflash" + args.revstring[0] + ".repo "
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        zyppclean = ZYPPER_CMD + " clean "
        try:
            ps1 = subprocess.Popen(zyppclean.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_debian_repo(args, fetchurl, ubuntutype):
    global rocklist

    if args.repourl:
        pass
    else:
        # Set up rocm repo for chosen rev to install
        wgetkey = WGET_CMD + " -q -O - http://repo.radeon.com/fwupdator/amdfw.gpg.key "
        aptkeycmd = APTKEY_CMD + " add -"
        try:
            ps1 = subprocess.Popen(wgetkey.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(aptkeycmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # use rev specific rocm repo
        debrepo = "deb [arch=amd64] " + fetchurl + " " + ubuntutype + " main "
        echocmd = ECHO_CMD + " '" + debrepo + "' "
        repofilename = "/etc/apt/sources.list.d/amdfwflash" + args.revstring[0] + ".list "
        teecmd = TEE_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # apt update repo
        aptupdate = APT_CMD + " clean"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # apt update repo
        aptupdate = APT_CMD + " update"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)



def remove_debian_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/apt/sources.list.d/amdfwflash" + args.revstring[0] + ".list "
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        # apt update repo
        aptupdate = APT_CMD + " clean"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)



#
# --rev REV is the ROCm version number string
# --destdir DESTDIR directory to download rpm for installation
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('[V1.0]amdfwflashinst.py: utility to '
        ' download and install amdfwflash IFWI Updator package for specified rev'
        ' (requires sudo privilege) '),
        prefix_chars='-')
    parser.add_argument('--rev', nargs=1, dest='revstring', default='rpm',
        help=('specifies release version '
              ' Example: --rev 1.0 for amdfwflash 1.0'
              )
              )
    parser.add_argument('--destdir', nargs=1, dest='destdir', default='.',
        help=('specify directory where to download RPM'
              ' before installation. Default: current directory '
              ' --destdir /tmp to use /tmp directory')
              )
    parser.add_argument('--update', dest='updateifwi', action='store_true',
        help=('update the ifwi after the packages are installed'
              ' to the new version ')
              )
    parser.add_argument('--rollback', dest='rollbackifwi', action='store_true',
        help=('rollback the ifwi after the packages are installed'
              ' to the GA version ')
              )
    parser.add_argument('--list', dest='listonly', action='store_true',
        help=('just list the packages that will be installed'
              ' -- do not download or install ')
              )
    parser.add_argument('--repourl', nargs=1, dest='repourl', default=None,
        help=('specify repo URL to use from where to download packages'
              ' as in http://repo.radeon.com/fwupdator/{apt, yum, zyp, centos8}/<REV> '
              ' Example: --repourl http://compute-artifactory/build/xyz')
              )
    parser.add_argument('--baseurl', nargs=1, dest='baseurl', default=None,
        help=('specify early access repo URL to use from where to download packages'
              ' as in http://repo.radeon.com/fwupdator/{apt, yum, zyp, centos8}/.. '
              ' Example: --baseurl http://repo.radeon.com/fwupdator/private/bionic/')
              )

    args = parser.parse_args();

    # Determine installed OS type
    ostype = None
    with open(ETC_OS_RELEASE, 'r') as f:
        for line in f:
            if CENTOS_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
                break
            if DEBIAN_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                break
            if JAMMY_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = JAMMY_TYPE
                break
            if FOCAL_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = FOCAL_TYPE
                break
            if BIONIC_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = BIONIC_TYPE
                break
            if SLES_TYPE.lower() in line.lower():
                ostype = SLES_TYPE
                break
            if RHEL_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
                break

    # Detect CentOS8/RHEL8 to set the correct ROCm repo
    if ostype is CENTOS_TYPE:
        with open(ETC_OS_RELEASE, 'r') as f:
            for line in f:
                if CENTOS_VERSION8_TYPESTRING.lower() in line.lower():
                    ostype = CENTOS8_TYPE
                    break
                if RHEL_VERSION8_TYPESTRING.lower() in line.lower():
                    ostype = CENTOS8_TYPE
                    break
                if CENTOS_VERSION9_TYPESTRING.lower() in line.lower():
                    ostype = RHEL9_TYPE
                    break
                if RHEL_VERSION9_TYPESTRING.lower() in line.lower():
                    ostype = RHEL9_TYPE
                    break

    if ostype is None:
        print("Exiting: Unknown installed OS type")
        parser.print_help()
        sys.exit(1)

    # Log version and date of run
    print("Running V0.3 amdfwflashinst.py utility for OS: " + ostype + " on: " + str(datetime.datetime.now()))

    if is_amdgpu_driver_loaded():
        print("amdgpu driver is LOADED. Please blacklist amdgpu and try again")
		sys.exit(0)
    else:
        print("amdgpu driver is NOT LOADED")

    #
    # Set pkgtype to use based on ostype
    #
    pkgtype = None
    pkgtype = {
        RHEL9_TYPE : PKGTYPE_RPM,
        RHEL8_TYPE : PKGTYPE_RPM,
        CENTOS8_TYPE : PKGTYPE_RPM,
        CENTOS_TYPE : PKGTYPE_RPM,
        UBUNTU_TYPE : PKGTYPE_DEB,
        SLES_TYPE : PKGTYPE_RPM
    }[ostype]

    #
    # Get the list of package names from repo using --rev option
    #
    if args.repourl:
        fwbaseurl = args.repourl[0]
    elif args.baseurl:
        fwbaseurl = args.baseurl[0]
    else:
        if args.revstring[0] in fwupdatorurl:
            fwbaseurl = fwupdatorurl[args.revstring[0]][ostype]
        else:
            print("Exiting: No AMDFWFLASH package for specified rev: ", args.revstring[0])
            sys.exit(1)

    #
    # Based on os type, set the package install command and options
    #
    cmd = {
       RHEL9_TYPE : YUM_CMD + " install --assumeyes amdfwflash ",
       RHEL8_TYPE : YUM_CMD + " install --assumeyes amdfwflash ",
       CENTOS8_TYPE : YUM_CMD + " install --assumeyes  amdfwflash",
       CENTOS_TYPE : YUM_CMD + " install --assumeyes amdfwflash",
       UBUNTU_TYPE : APTGET_CMD + " -y install amdfwflash",
       SLES_TYPE : ZYPPER_CMD + " install amdfwflash "
    }[ostype]

    #
    # If --list specified, print the package list and exit
    #
    if args.listonly is True:
        print("List device\n")
        list_devices()
        sys.exit(0)

    # for Ubuntu/Debian
    if ostype is UBUNTU_TYPE:
        setup_debian_repo(args, fwbaseurl, "ubuntu")
    elif ostype is CENTOS_TYPE:
        setup_centos_repo(args, fwbaseurl)
    elif ostype is CENTOS8_TYPE:
        setup_centos8_repo(args, fwbaseurl)
    elif ostype is RHEL9_TYPE:
        setup_centos9_repo(args, fwbaseurl)
    else:
        if is_iomem_relaxed_set() is True:
            print("Detected: iomem=relaxed boot paramter set.")
            setup_sles_zypp_repo(args, fwbaseurl)
        else:
            print("SLES15 requires iomem=relaxed boot parameter set.")
            print("NOTE: Please refer to the AMDFWFLASH User Guide.")
            sys.exit(0)

    try:
        ps1 = subprocess.Popen(cmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")

    if args.updateifwi is True:
        print("Update IFWI")
        update_ifwi()
    elif args.rollbackifwi is True:
        print("Rollback IFWI")
        rollback_ifwi()

    if ostype is CENTOS_TYPE or ostype is CENTOS8_TYPE or ostype is RHEL9_TYPE:
        remove_centos_repo(args, fwbaseurl)
    elif ostype is UBUNTU_TYPE:
        remove_debian_repo(args, fwbaseurl)
    else:
        remove_sles_zypp_repo(args, fwbaseurl)
        remove_iomem_relaxed_param()

    sys.exit(0)
