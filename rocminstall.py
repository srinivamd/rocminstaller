#!/usr/bin/env python3
#
# Copyright (c) 2020 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
#
# Download and install a specific ROCm version
# V1.1: Initial version 4/12/2010
#   No support for Debian/Ubuntu, Only supports CentOS/SLES
#
from urllib import request
from urllib.request import urlretrieve
import re
import subprocess
import sys
import argparse

# Set ROCm Release Package Distribution repo baseURL below
# External ROCM release baseurl for rpm/yum: http://repo.radeon.com/rocm/yum
rocmyum_base = "http://repo.radeon.com/rocm/yum/"
rocmapt_base = "http://repo.radeon.com/rocm/apt/"
rocmzyp_base = "http://repo.radeon.com/rocm/zyp/"

# Commands
RPM_CMD = "/usr/bin/rpm"
DPKG_CMD = "/usr/bin/dpkg"
ZYPPER_CMD = "/usr/bin/zypper"

# Package type suffixes
PKGTYPE_RPM = "rpm"
PKGTYPE_DEB = "deb"

# Supported OS types
CENTOS_TYPE = "centos"
UBUNTU_TYPE = "ubuntu"
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
    try:
        ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, check=True)
        print(ps1.stdout)
        return True
    except subprocess.CalledProcessError as err:
        return False

# Get the list of ROCm rpm packages from the ROCm release URL
pkglist = []
pkgset = set()
def get_pkglist(rocmurl, revstring, pkgtype):
    global pkglist
    urlpath = rocmurl
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'".*\.{pkgtype}"', line)
            if mat:
                pkgname = line[mat.start()+1:mat.end()-1]
                # MIOpen-HIP conflicts with MIOpen-OpenCL from same repo
                if "MIOpen-OpenCL" in pkgname:  # ignore, conflicts w MIOpen-HIP
                    continue
                #
                # TODO XXX: adjust revstring to X.Y if it is X.Y.Z
                if not re.search(rf'[a-zA-Z]+{revstring}', pkgname) and not re.search(rf'[a-zA-Z]+64{revstring}', pkgname):
                    pkgset.add(pkgname)
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms from list
            print(" Skipping rock-dkms: a version is already installed.")
            print((" To install rock-dkms package, please remove installed rock-dkms"
                   " first. Reboot may be required. "))
            pkglist = [ x for x in pkgset if "rock-dkms" not in x ]
        else:
            pkglist = list(pkgset);
    except Exception as e:
        pkglist = None
        print(urlpath + " : " + str(e))

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
    args = parser.parse_args();

    # Determine installed OS type
    ostype = None
    with open(ETC_OS_RELEASE, 'r') as f:
        for line in f:
            if CENTOS_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
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
    rocmbaseurl = {
        CENTOS_TYPE : rocmyum_base,
        UBUNTU_TYPE : rocmapt_base,
        SLES_TYPE : rocmzyp_base
    }[ostype]

    get_pkglist(rocmbaseurl + "/" + args.revstring[0], args.revstring[0], pkgtype)

    #
    # Based on os type, set the package install command and options
    #
    cmd = {
       CENTOS_TYPE : RPM_CMD + " -ivh --nodeps --force ",
       UBUNTU_TYPE : DPKG_CMD + " -ivh ",
       SLES_TYPE : RPM_CMD + " -ivh --nodeps --force "
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
            '\n'.join(sorted(pkglist)))
        sys.exit(0)

    #
    # Download and install the selected packages
    #
    for n in sorted(pkglist):
        urlretrieve(rocmbaseurl + "/" + args.revstring[0] + "/" + n,
            args.destdir[0] + "/" + n) # download destdir
        execcmd = cmd + args.destdir[0] + "/" + n
        try:
            ps1 = subprocess.run(execcmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout)
            ps2 = subprocess.run(["/bin/rm", "-f", args.destdir[0] + "/" + n],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False);
            print(ps2.stdout)
        except subprocess.CalledProcessError as err:
            print(err.output)
            print(" Unexpected error encountered! Did you forget sudo?")
            ps2 = subprocess.run(["/bin/rm", "-f", args.destdir[0] + "/" + n],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False);
            print(ps2.stdout)
            break
#
    sys.exit(0)
