#!/bin/sh
#
# Copyright (c) 2021 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
#
# Script to uninstall ROCm X.Y.Z version packages, excluding kernel modules
#
# Usage: sudo ./rocmuninstall.sh X.Y.Z
#    where X.Y.Z is the version of ROCm to be UNINSTALLED
# Example: To uninstall ROCm 4.1.0 packages (excluding kernel modules)
#   sudo ./rocmuninstall.sh 4.1.0
#
# NOTE: To uninstall rock-dkms, rock-dkms-firmware ROCm kernel modules
#       manually uninstall them and reboot the system
# V1.1: Fix CentOS uninstall
# V1.0: Initial version
#
echo "=== ROCm Uninstall Utility V1.1 ==="
/bin/date

if [ $# -ne 1 ]
then
	echo "Usage: sudo $0 <X.Y.Z>|all, where <X.Y.Z> is the ROCm version to uninstall"
	echo " To uninstall all ROCm packages (except kernel) use 'all' option"
	echo " Example: To uninstall ROCm 4.1 packages use:"
	echo "    sudo sh ./rocmuninstall.sh 4.1.0 "
	echo " Example: To uninstall all ROCm packages use:"
	echo "    sudo sh ./rocmuninstall.sh all "
	echo " User will be prompted with list of selected packages to confirm uninstallation."
	exit 1
fi
# Detect OS type
ret=`/bin/grep -i -E 'debian|ubuntu' /etc/os-release`
if [ $? -ne 0 ]
then
    ret=`/bin/grep -i -E 'centos|rhel' /etc/os-release`
    if [ $? -ne 0 ]
    then
        pkgtype="sles"
    else
        pkgtype="rpm"
    fi
else
    pkgtype="deb"
fi

export REV=$1

if [ ${REV} = "all" ]
then
    echo "Remove ALL ROCm packages"
    if [ "$pkgtype" = "deb" ]
    then
        pkglist=`/usr/bin/dpkg -l | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|^ii  hip|hcc|hsa|rocm|atmi|^ii  comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rdc|openmp-' | /usr/bin/awk '!/Status/ {print $2}' | /usr/bin/sort`
    else
        pkglist=`/usr/bin/rpm -qa | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|hip|hcc|hsa|rocm|atmi|comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rdc|openmp-' | /usr/bin/sort`
    fi
else
    echo "Remove ROCm packages for release $REV"
    if [ "$pkgtype" = "deb" ]
    then
        pkglist=`/usr/bin/dpkg -l | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|^ii  hip|hcc|hsa|rocm|atmi|^ii  comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rdc|openmp-' | /usr/bin/awk '!/Status/ {print $2}' | /bin/grep -E '^[a-zA-Z\-]+[a-zA-Z]'${REV}'|^[a-zA-Z\-]+lib64'${REV}'|^miopenkernels-gfx.*'${REV} | /usr/bin/sort`
    else
        pkglist=`/usr/bin/rpm -qa | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|hip|hcc|hsa|rocm|atmi|comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rdc|openmp-' | /bin/grep -E '^[a-zA-Z\-]+[a-zA-Z]'${REV}'|^[a-zA-Z\-]+lib64'${REV}'|^miopenkernels-gfx.*'${REV} | /usr/bin/sort`
    fi
fi

# List the ROCm packages that will be uninstalled
echo "List of packages selected for uninstall: "
echo $pkglist

# Prompt user
while true; do
    read -p "Do you want to continue to uninstall above packages [Y/n]?" ans
    case $ans in
        [Yy]* ) echo "Uninstalling...";
	    if [ "$pkgtype" = "deb" ]
	    then
                /usr/bin/apt remove $pkglist;
	    elif [ "$pkgtype" = "rpm" ]
	    then
                /usr/bin/yum remove $pkglist;
	    else
                /usr/bin/zypper remove $pkglist;
	    fi
	    break;;
        [Nn]* ) echo "Aborting."; break;;
        * ) echo "Please answer yes or no to continue.";;
    esac
done
