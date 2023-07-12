# [Unofficial] ROCM Installer TL;DR (see Pre-Install Steps for your OS Distro)
***Steps to install/uninstall ROCm (multiple releases side-by-side or single version)***
#### Pre-install step: Upgrade OS to get latest kernel headers, etc.
1. Download amdgpuinst.py script, install ROCm AMDGPU DKMS packages and reboot:
```
  wget -O amdgpuinst.py --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/amdgpuinst.py

Example: Install ROCm DKMS/kernel packages amdgpu-dkms and amdgpu-dkms-firmware
  sudo python3 ./amdgpuinst.py --rev 5.5.0
  sudo reboot
```
2. Download rocminstall.py script to install ROCm User Level Packages:
```
  wget -O rocminstall.py --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py
Example: Install ROCm [add --nomiopenkernels to exclude pre-built miopenkernels]
  sudo python3 ./rocminstall.py --rev 5.5
```
#### UNINSTALL AMDGPU DRIVER
1. To uninstall AMDGPU driver, uninstall `amdgpu-core`, `amdgpu-dkms` and `amdgpu-dkms-firmware` packages and reboot:
```
On Ubuntu:
   sudo apt remove amdgpu-core amdgpu-dkms amdgpu-dkms-firmware
   sudo reboot
On RHEL, SLES:
   sudo yum remove amdgpu-core amdgpu-dkms amdgpu-dkms-firmware
   sudo reboot
```
#### UNINSTALL ROCM
1. To uninstall ROCm, download the rocmuninstall.sh script, run with version or "all":
```
 wget -O rocmuninstall.sh --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocmuninstall.sh

Example: To uninstall ROCm 5.5 packages use (requires sudo):
    sudo sh ./rocmuninstall.sh 5.5.0  [use "all" to uninstall user AND kernel packages]
```
# [Unofficial] V1.62 rocminstall.py Utility to install ROCm releases. Supports Ubuntu/Debian, CentOS/RHEL 7/8, SLES15 installation
#### NOTE: Install dkms, kernel headers, gcc packages on OS BEFORE installing ROCm Kernel

## Section CentOS Pre-Install Steps (Install Perl dependencies)
**CentOS 7/8 Preparing System for ROCm Kernel:**
```
  sudo yum clean all
  sudo yum update (this would update kernel to latest. Do this before installing kernel-headers.)
  sudo reboot
  sudo yum install kernel-headers-`uname -r`
  sudo yum install gcc
  sudo yum install gcc-c++
  sudo yum install -y epel-release
  RHEL8:
    sudo subscription-manager repos --enable codeready-builder-for-rhel-8-$(arch)-rpms
    sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
  RHEL9:
    sudo subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
    sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
  RockyLinux9:
    sudo dnf --enablerepo=crb install perl-File-BaseDir
  sudo yum install dkms
  sudo yum install kernel-devel-`uname -r`
  sudo yum install python3
  sudo yum install wget
  sudo yum install git
  sudo yum install perl
  sudo yum install perl-URI-Encode
  sudo reboot (for above updates to take effect)
  NOTE: install devtoolset-7 for CentOS7/RHEL7
```
#### To remove ROCm Kernel (amdgpu-dkms amdgpu-dkms-firmware) Packages:
**CentOS/RHEL rpm Commands to UNINSTALL amdgpu-dkms amdgpu-dkms-firmware packages FIRST before install**
```
  sudo rpm -evh amdgpu-dkms amdgpu-dkms-firmware (OR sudo rpm -evh --nodeps amdgpu-dkms amdgpu-dkms-firmware)
  sudo reboot
```

## Section: Ubuntu Pre-Install Steps
**Ubuntu 18 HWE Preparing System for ROCm Kernel**
```
   sudo apt-get install --install-recommends linux-generic-hwe-18.04  (Use linux-generic-hwe-20.04 for Ubuntu 20.04 HWE.) 
   (Update to LTS HWE before installing linux-headers.)
   sudo reboot
   sudo apt install dkms
   sudo apt install gcc
   sudo apt install g++
   sudo apt upgrade (this may be needed for kernel updates to correspond with headers, etc.)
   sudo reboot (for above upgrade to take effect)
   sudo apt install linux-headers-`uname -r`
   sudo apt install linux-tools-`uname -r`
   sudo reboot
```
#### To Update ROCm Kernel (amdgpu-dkms amdgpu-dkms-firmware) Packages:
**Ubuntu dpkg Commands to UNINSTALL ROCm amdgpu-dkms amdgpu-dkms-firmware packages FIRST before install**
```
  sudo dpkg -r --force-all amdgpu-dkms amdgpu-dkms-firmware
  sudo dpkg --purge --force-all amdgpu-dkms amdgpu-dkms-firmware
  sudo reboot
```
#### NOTE: On SLES15, the script uses zypper and requires user interaction

## Section: Install ROCm
#### Download Python3 rocminstall.py script:
***wget -O rocminstall.py --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py***

```
Example: Install ROCm, including kernel components (assumes dkms, kernel header, gcc preinstalled)
  wget -O rocminstall.py --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py

Example: Install ROCm, excluding pre-built miopenkernels (faster install)
  sudo python3 ./rocminstall.py --rev 5.5 --nomiopenkernels

Example: Install ROCm including pre-built miopenkernels
  sudo python3 ./rocminstall.py --rev 5.5

Example: Install ROCm packages in container (no kernel components)
  sudo python3 ./rocminstall.py --rev 5.4.3 --nokernel

```
#### Usage
```
usage: rocminstall.py [-h] [--rev REVSTRING] [--destdir DESTDIR] [--list]
                      [--repourl REPOURL] [--baseurl BASEURL] [--nokernel]
                      [--justkernel] [--justrdc] [--nomiopenkernels]

[V1.62]rocminstall.py: utility to download and install ROCm packages for
specified rev (dkms, kernel headers must be installed, requires sudo
privilege)

optional arguments:
  -h, --help         show this help message and exit
  --rev REVSTRING    specifies ROCm release repo to use as in
                     http://repo.radeon.com/rocm/{apt, yum, zyp,
                     centos8}/<REV> Example: --rev 3.5 for ROCm 3.5 repo
                     http://repo.radeon.com/rocm/{apt, yum, zyp, centos8}/3.5,
                     or --rev 3.3 for ROCm 3.3 repo
                     http://repo.radeon.com/rocm/{apt, yum, zyp}/3.3
  --destdir DESTDIR  specify directory where to download RPM before
                     installation. Default: current directory --destdir /tmp
                     to use /tmp directory
  --list             just list the packages that will be installed -- do not
                     download or install
  --repourl REPOURL  specify ROCm repo URL to use from where to download
                     packages Example: --repourl http://compute-
                     artifactory/build/xyz
  --baseurl BASEURL  specify early access ROCm repo URL to use from where to
                     download packages Example: --baseurl
                     http://repo.radeon.com/rocm/private/apt_3.6-priv/
  --nokernel         do not install amdgpu kernel packages, for example, used to
                     install ROCm in docker
  --justkernel       ONLY install amdgpu kernel packages of specified version -
                     undefined behavior if --nokernel also specified
  --justrdc          ONLY install ROCm Radeon Data Center Monitor tool -
                     attempts to install rdcX.Y.Z package corresponding to rev
  --nomiopenkernels  do not install pre-built miopenkernels packages - saves
                     space and installation time

```
# [Unofficial] V1.40 ROCm AMDGPU DKMS Install Utility (amdgpuinst.py)
## NOTE: This can be used to amdgpu-dkms* packages for ROCm release starting with 4.5
## Currently, only support 4.5 and newer releases
#
### Usage: To install ROCm kernel packages
```
Download the Python3 script:
  wget -O amdgpuinst.py --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/amdgpuinst.py

Example: Install ROCm 5.6 kernel packages amdgpu-dkms and amdgpu-dkms-firmware
  sudo python3 ./amdgpuinst.py --rev 5.6.0

Example: List ROCm 5.6 kernel packages amdgpu-dkms and amdgpu-dkms-firmware
  sudo python3 ./amdgpuinst.py --rev 5.6.0 --list

Example: List ROCm 5.4.3 kernel packages amdgpu-dkms and amdgpu-dkms-firmware
  sudo python3 ./amdgpuinst.py --rev 5.4.3 --list

```

# [Unofficial] Interactive ROCm Uninstall Utility
## NOTE: Does not uninstall ROCm Kernel packages (amdgpu-dkms amdgpu-dkms-firmware) 
##       unless "all" option is specified
#### To uninstall ROCm kernel
**CentOS/RHEL rpm Commands to UNINSTALL amdgpu-dkms amdgpu-dkms-firmware packages ONLY**
```
  sudo rpm -evh amdgpu-dkms amdgpu-dkms-firmware (OR sudo rpm -evh --nodeps amdgpu-dkms amdgpu-dkms-firmware)
  sudo reboot
```
**Ubuntu Commands to UNINSTALL amdgpu-dkms amdgpu-dkms-firmware packages ONLY**
```
  sudo apt remove amdgpu-core amdgpu-dkms amdgpu-dkms-firmware
  sudo reboot
```

### Steps to Run rocmuninstall.sh Script
#### Download the rocmuninstall.sh shell script:
***wget -O rocmuninstall.sh --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocmuninstall.sh***
#### NOTE: User will be prompted with list of selected packages to confirm uninstallation.

```
Examples
# Download the rocmuninstall.sh script
 wget -O rocmuninstall.sh --no-cache --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocmuninstall.sh

 Example: To uninstall ROCm packages use (requires sudo):
    sudo sh ./rocmuninstall.sh 5.1.0  [Note: uninstalls version 5.1.0 packages]

 Example: To uninstall all ROCm packages use (requires sudo):
    sudo sh ./rocmuninstall.sh all 
```
#### Usage of rocmuninstall.sh script
```
=== ROCm Uninstall Utility V1.6 ===
Mon May  3 15:39:50 PDT 2021
Usage: sudo sh ./rocmuninstall.sh <X.Y.Z>|all, where <X.Y.Z> is the ROCm version to uninstall
 To uninstall all ROCm packages (except kernel) use 'all' option
 Example: To uninstall ROCm 4.1 packages use:
    sudo sh ./rocmuninstall.sh 4.1.0 
 Example: To uninstall all ROCm packages use:
    sudo sh ./rocmuninstall.sh all 
 User will be prompted with list of selected packages to confirm uninstallation.
```

