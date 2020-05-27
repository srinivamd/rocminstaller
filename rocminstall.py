#!/usr/bin/env python3
#
# Copyright (c) 2020 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
#
# Download and install a specific ROCm version
# V1.4: Added support for debian/ubuntu
#       SLES broken, zypper non-interactive defaults a pain
# V1.3: Use yum on SLES
#       Add support for Debian/Ubuntu
# V1.2: Install with dependencies using yum
#       Handle 3.1.1 as special case
#       Download all RPMs then install using yum (no --force install)
#       Use --skip-broken to skip broken packages
# V1.1: Initial version 4/12/2010
#   No support for Debian/Ubuntu, Only supports CentOS/SLES
#
from urllib import request
from urllib.request import urlretrieve
import re
import subprocess
import sys
import argparse
import os

# Set ROCm Release Package Distribution repo baseURL below
# External ROCM release baseurl for rpm/yum: http://repo.radeon.com/rocm/yum
rocmyum_base = "http://repo.radeon.com/rocm/yum/"
rocmapt_base = "http://repo.radeon.com/rocm/apt/"
rocmzyp_base = "http://repo.radeon.com/rocm/zyp/"
# Internal builds
internal_rocmyum_base = "http://compute-artifactory.amd.com/artifactory/list/rocm-osdb-rpm/compute-rocm-dkms-no-npi-hipclang-2275/"
internal_rocmdeb_base = "http://compute-artifactory.amd.com/artifactory/list/rocm-osdb-deb/compute-rocm-dkms-no-npi-hipclang-2275/"

# Commands
RM_F_CMD = "/bin/rm -f "
RPM_CMD = "/usr/bin/rpm"
YUM_CMD = "/usr/bin/yum"
DPKG_CMD = "/usr/bin/dpkg"
APTGET_CMD = "/usr/bin/apt-get"
ZYPPER_CMD = "/usr/bin/zypper"

# Package type suffixes
PKGTYPE_RPM = "rpm"
PKGTYPE_DEB = "deb"

# Supported OS types
CENTOS_TYPE = "centos"
UBUNTU_TYPE = "ubuntu"
DEBIAN_TYPE = "debian"
SLES_TYPE = "sles"

# OS release info
ETC_OS_RELEASE = "/etc/os-release"
# Download destination dir: default current director
DOWNLOAD_DESTDIR = "./"

#
# Is rock-dkms already installed? True if already installed
#
def check_rock_dkms(pkgtype):
    check_cmd = {
        PKGTYPE_RPM : RPM_CMD + " -q rock-dkms ",
        PKGTYPE_DEB : DPKG_CMD + " -l rock-dkms ",
    }[pkgtype]
    if pkgtype is PKGTYPE_RPM:
        check_cmd = RPM_CMD + " -q rock-dkms "
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            return True
        except subprocess.CalledProcessError as err:
            return False
    elif pkgtype is PKGTYPE_DEB:
        check_cmd = DPKG_CMD + " -l rock-dkms "
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            for line in str.splitlines(ps1.stdout.decode('utf-8')):
                if re.search(r'^i.*rock-dkms.*all', line): # 'i' for installed
                    return True
            return False
        except subprocess.CalledProcessError as err:
            return False
    else:
        print("Unknown package type {}. Cannot detect rock-dkms status.".format(pkgtype))
        return False

# Get the list of ROCm rpm packages from the ROCm release URL
pkglist = []
pkgset = set()
rockset = set()
rocklist = []
# debian/ubuntu
def get_deb_pkglist311(rocmurl, revstring, pkgtype):
    global pkglist
    global rocklist
    urlpath = rocmurl + "/dists/xenial/main/binary-amd64/Packages"
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'Filename: pool.*\.{pkgtype}', line)
            if mat:
                pkgname = line[mat.start()+len("Filename: "):mat.end()]
                # MIOpen-HIP conflicts with MIOpen-OpenCL from same repo
                if ("MIOpen-OpenCL".lower() in pkgname.lower()  # ignore, conflicts w MIOpen-HIP
                    or "MIVisionX".lower() in pkgname.lower()
                    or "hip-nvcc".lower() in pkgname.lower()
                    or "hip_nvcc".lower() in pkgname.lower()):
                        continue
                #
                if "rock-dkms".lower() in pkgname.lower():
                    rockset.add(pkgname)
                    continue
                #
                if (not re.search(rf'[a-zA-Z]+{revstring}', os.path.basename(pkgname))
                    and not re.search(rf'[a-zA-Z]+64{revstring}', os.path.basename(pkgname))):
                        pkgset.add(pkgname)
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" Skipping rock-dkms: a version is already installed.")
            print((" To install rock-dkms package, please remove installed rock-dkms"
                   " first. Reboot may be required. "))
            pkglist = [ x for x in pkgset if "rock-dkms" not in x ]
            rocklist = []
        else:
            pkglist = list(pkgset)
            rocklist = list(rockset)
    except Exception as e:
        pkglist = None
        rocklist = None
        print(urlpath + " : " + str(e))

# get pkglist for 3.1.1
def get_pkglist311(rocmurl, revstring, pkgtype):
    global pkglist
    global rocklist
    urlpath = rocmurl
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'".*\.{pkgtype}"', line)
            if mat:
                pkgname = line[mat.start()+1:mat.end()-1]
                # MIOpen-HIP conflicts with MIOpen-OpenCL from same repo
                if ("MIOpen-OpenCL".lower() in pkgname.lower()
                    or "MIVisionX".lower() in pkgname.lower()
                    or "hip-nvcc".lower() in pkgname.lower()
                    or "hip_nvcc".lower() in pkgname.lower()):
                    continue
                #
                if "rock-dkms".lower() in pkgname.lower():
                    rockset.add(pkgname)
                    continue
                # TODO XXX: adjust revstring to X.Y if it is X.Y.Z
                if (not re.search(rf'[a-zA-Z]+{revstring}', pkgname)
                    and not re.search(rf'[a-zA-Z]+64{revstring}', pkgname)):
                    pkgset.add(pkgname)
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" Skipping rock-dkms: a version is already installed.")
            print((" To install rock-dkms package, please remove installed rock-dkms"
                   " first. Reboot may be required. "))
            pkglist = [ x for x in pkgset if "rock-dkms" not in x ]
            rocklist = []
        else:
            pkglist = list(pkgset)
            rocklist = list(rockset)
    except Exception as e:
        pkglist = None
        rocklist = None
        print(urlpath + " : " + str(e))

#
# get pkglist for release 3.3 and newer
# select packages with names pkgX.Y.Z
#
# debian/ubuntu
def get_deb_pkglist(rocmurl, revstring, pkgtype):
    global pkglist
    global rocklist
    urlpath = rocmurl + "/dists/xenial/main/binary-amd64/Packages"
    patrevstr = revstring[0:2] # adjust search pattern to X.Y
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'Filename: pool.*\.{pkgtype}', line)
            if mat:
                pkgname = line[mat.start()+len("Filename: "):mat.end()]
                # MIOpen-HIP conflicts with MIOpen-OpenCL from same repo
                if ("MIOpen-OpenCL".lower() in pkgname.lower()  # ignore, conflicts w MIOpen-HIP
                    or "MIVisionX-nvcc".lower() in pkgname.lower()
                    or "hip-nvcc".lower() in pkgname.lower()
                    or "hip_nvcc".lower() in pkgname.lower()):
                        continue
                if "rock-dkms".lower() in pkgname.lower():
                    rockset.add(pkgname)
                    continue
                #
                # Use X.Y part of X.Y.Z revstring
                # 
                if (re.search(rf'^[a-zA-Z\-]+[a-zA-Z]{patrevstr}', os.path.basename(pkgname))
                    or re.search(rf'^[a-zA-Z\-]+lib64{patrevstr}', os.path.basename(pkgname))):
                        pkgset.add(pkgname)
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" Skipping rock-dkms: a version is already installed.")
            print((" To install rock-dkms package, please remove installed rock-dkms"
                   " first. Reboot may be required. "))
            pkglist = [ x for x in pkgset if "rock-dkms" not in x ]
            rocklist = []
        else:
            pkglist = list(pkgset)
            rocklist = list(rockset)
    except Exception as e:
        pkglist = None
        rocklist = None
        print(urlpath + " : " + str(e))

def get_pkglist(rocmurl, revstring, pkgtype):
    global pkglist
    global rocklist
    urlpath = rocmurl
    patrevstr = revstring[0:2] # adjust pat to X.Y
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'".*\.{pkgtype}"', line)
            if mat:
                pkgname = line[mat.start()+1:mat.end()-1]
                # MIOpen-HIP conflicts with MIOpen-OpenCL from same repo
                # default is MIOpen-HIP
                if ("MIOpen-OpenCL".lower() in pkgname.lower()
                    or "MIVisionX".lower() in pkgname.lower()
                    or "hip-nvcc".lower() in pkgname.lower()
                    or "hip_nvcc".lower() in pkgname.lower()):
                        continue
                if "rock-dkms".lower() in pkgname.lower():
                    rockset.add(pkgname)
                    continue
                #
                # Use X.Y part of X.Y.Z revstring
                # 
                if (re.search(rf'^[a-zA-Z\-]+[a-zA-Z]{patrevstr}', pkgname)
                    or re.search(rf'^[a-zA-Z\-]+lib64{patrevstr}', pkgname)):
                        pkgset.add(pkgname)
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" Skipping rock-dkms: a version is already installed.")
            print((" To install rock-dkms package, please remove installed rock-dkms"
                   " first. Reboot may be required. "))
            pkglist = [ x for x in pkgset if "rock-dkms" not in x ]
            rocklist = []
        else:
            pkglist = list(pkgset)
            rocklist = list(rockset)
    except Exception as e:
        pkglist = None
        rocklist = None
        print(urlpath + " : " + str(e))

def download_and_install_deb(args, rocmbaseurl, pkgname):
    global pkglist
    global rocklist
    # Download and Install rock-dkms-firmware first (assumes only one)
    rmcmd = RM_F_CMD
    dpkgicmd = DPKG_CMD + " -i "
    aptinstcmd = APTGET_CMD + " -y -f install "
    urlretrieve(rocmbaseurl + "/" + args.revstring[0] + "/" + pkgname,
        args.destdir[0] + "/" + os.path.basename(pkgname)) # download destdir
    execcmd = dpkgicmd + args.destdir[0] + "/" + os.path.basename(pkgname) + " "
    rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(pkgname) + " "
    try:
        ps1 = subprocess.run(execcmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        for line in str.splitlines(ps1.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
    try:
        ps1 = subprocess.run(aptinstcmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        for line in str.splitlines(ps1.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
    try:
        ps2 = subprocess.run(rmcmd.split(),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False);
        for line in str.splitlines(ps2.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")


# On Ubuntu, use the steps below to install downloaded deb
# 1. Install rock-dkms-firmware dpkg -i rock-dkms-firmware
# 2. Install rock-dkms: dpkg -i rock-dkms
# 3. Fix rock-dkms install dependencies: apt-get -y -f install
# 4. Remove rock-dkms-firmware, rock-dkms
# 5. Install the remaining downloaded deb: dpkg -i *.deb
# 6. Remove remaining deb packages
def download_install_rocm_deb(args, rocmbaseurl):
    global pkglist
    global rocklist
    rmcmd = RM_F_CMD
    dpkgicmd = DPKG_CMD + " -i "
    aptinstcmd = APTGET_CMD + " -y -f install "
    pkgn = [ x for x in rocklist if "rock-dkms-firmware" in x ]
    if pkgn:
        # remove rock-dkms-firmware from list
        rocklist = [ x for x in rocklist if "rock-dkms-firmware" not in x ]
        # Download and Install rock-dkms-firmware first (assumes only one)
        download_and_install_deb(args, rocmbaseurl, pkgn[0])
    pkgn = [ x for x in rocklist if "rock-dkms" in x ]
    if pkgn:
        # Download and Install rock-dkms
        download_and_install_deb(args, rocmbaseurl, pkgn[0])

    # Install the rest of the deb packages
    rmcmd = RM_F_CMD
    dpkgicmd = DPKG_CMD + " -i "
    execcmd = dpkgicmd
    for n in sorted(pkglist):
        urlretrieve(rocmbaseurl + "/" + args.revstring[0] + "/" + n,
            args.destdir[0] + "/" + os.path.basename(n)) # download destdir
        execcmd = execcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        print('.', end='', flush=True)
    try:
        ps1 = subprocess.run(execcmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        for line in str.splitlines(ps1.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)

    try:
        ps1 = subprocess.run(aptinstcmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        for line in str.splitlines(ps1.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)

    try:
        ps2 = subprocess.run(rmcmd.split(),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False);
        for line in str.splitlines(ps2.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")

#
# --rev REV is the ROCm version number string
# --destdir DESTDIR directory to download rpm for installation
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('rocminstall.py: utility to '
        ' download and install ROCm RPMs for specified version'
        ' (requires sudo privilege) '),
        prefix_chars='-')
    parser.add_argument('--rev', nargs=1, dest='revstring', default='rpm',
        help=('specifies ROCm release repo to use '
              ' as in http://repo.radeon.com/rocm/{apt, yum zyp}/<REV> '
              ' Example: --rev 3.3 for ROCm 3.3 repo '
              ' http://repo.radeon.com/rocm/{apt, yum, zyp}/3.3, '
              ' or '
              ' --rev 3.1.1 for ROCm 3.1.1 repo '
              ' http://repo.radeon.com/rocm/{apt, yum, zyp}/3.1.1 ')
              )
    parser.add_argument('--destdir', nargs=1, dest='destdir', default='.',
        help=('specify directory where to download RPM'
              ' before installation. Default: current directory '
              ' --destdir /tmp to use /tmp directory')
              )
    parser.add_argument('--list', dest='listonly', action='store_true',
        help=('just list the packages that will be installed'
              ' -- do not download or install ')
              )
    parser.add_argument('--repourl', nargs=1, dest='repourl', default=None,
        help=('specify ROCm repo URL to use from where to download packages'
              ' Example: --repourl http://repo.radeon.com/rocm/yum/3.3 ')
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
            if UBUNTU_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                break
            if SLES_TYPE.lower() in line.lower():
                ostype = SLES_TYPE
    if ostype is None:
        print("Exiting: Unknown installed OS type")
        parser.print_help()
        sys.exit(1)

    #
    # Set pkgtype to use based on ostype
    #
    pkgtype = None
    pkgtype = {
        CENTOS_TYPE : PKGTYPE_RPM,
        UBUNTU_TYPE : PKGTYPE_DEB,
        SLES_TYPE : PKGTYPE_RPM
    }[ostype]

    #
    # Get the list of package names from repo using --rev option
    #
    if args.repourl:
        rocmbaseurl = args.repourl[0]
    else:
        rocmbaseurl = {
            CENTOS_TYPE : rocmyum_base,
            UBUNTU_TYPE : rocmapt_base,
            SLES_TYPE : rocmzyp_base
        }[ostype]

    if "3.1." in args.revstring[0]:
        if pkgtype is PKGTYPE_DEB:
            get_deb_pkglist311(rocmbaseurl + "/" + args.revstring[0], args.revstring[0],
                pkgtype)
        else:
            get_pkglist311(rocmbaseurl + "/" + args.revstring[0], args.revstring[0],
                pkgtype)
    elif args.repourl:
        get_pkglist(args.repourl[0] + "/", args.revstring[0], pkgtype)
    else:
        if pkgtype is PKGTYPE_DEB:
            get_deb_pkglist(rocmbaseurl + "/" + args.revstring[0], args.revstring[0],
                pkgtype)
        else:
            get_pkglist(rocmbaseurl + "/" + args.revstring[0], args.revstring[0],
                pkgtype)

    #
    # Based on os type, set the package install command and options
    #
    cmd = {
       CENTOS_TYPE : YUM_CMD + " localinstall --skip-broken --assumeyes ",
       UBUNTU_TYPE : APTGET_CMD + " --no-download --ignore-missing -y install ",
       SLES_TYPE : ZYPPER_CMD + " --non-interactive install --no-recommends "
    }[ostype]

    #
    # If pkglist is None, print help and exit
    #
    if pkglist is None:
        parser.print_help()
        sys.exit(1)

    #
    # If --list specified, print the package list and exit
    #
    if args.listonly is True:
        print("List of packages selected:\n" +
            '\n'.join(sorted(rocklist)) + '\n' +
            '\n'.join(sorted(pkglist)))
        sys.exit(0)

    #
    # Download and install the selected packages
    # Ubuntu/Debian dpkg/apt does not have an easy method to use dpkg, apt
    # to install downloaded deb packages with dependencies equivalent
    # yum localinstall command on CentOS, SLES.
    # So call a debian specific function for Ubuntu/Debian
    #
    # for Ubuntu/Debian
    if ostype is UBUNTU_TYPE:
        download_install_rocm_deb(args, rocmbaseurl)
        sys.exit(0)

    # for CentOS and SLES use the following
    execcmd = cmd
    rmcmd = RM_F_CMD
    for n in sorted(rocklist):
        urlretrieve(rocmbaseurl + "/" + args.revstring[0] + "/" + n,
            args.destdir[0] + "/" + os.path.basename(n)) # download destdir
        execcmd = execcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        print('.', end='', flush=True)

    for n in sorted(pkglist):
        urlretrieve(rocmbaseurl + "/" + args.revstring[0] + "/" + n,
            args.destdir[0] + "/" + os.path.basename(n)) # download destdir
        execcmd = execcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        print('.', end='', flush=True)

    try:
        ps1 = subprocess.run(execcmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        for line in str.splitlines(ps1.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")

    try:
        ps2 = subprocess.run(rmcmd.split(),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False);
        for line in str.splitlines(ps2.stdout.decode('utf-8')):
            print(line)
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
#
    sys.exit(0)
