#!/bin/sh
#
# Copyright (c) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
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
# V1.7: add new packages
# V1.6: fix SLES uninstall amdgpu
# V1.5: Add amdgpu-core
# V1.4: ROCm 4.5 support: Add amdgpu-dkms
# V1.3: Fix miopenkernel uninstall
# V1.2: Fix miopenkernel name match
# V1.1: Fix CentOS uninstall
# V1.0: Initial version
#
echo "=== ROCm Uninstall Utility V1.7 ==="
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
        pkglist=`/usr/bin/dpkg -l | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|^ii  hip|hcc|hsa|rocm|atmi|^ii  comgr|composa|amd-smi|aomp|amdgpu-core|amdgpu-dkms|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rocwmma|rpp|rdc|openmp-' | /usr/bin/awk '!/Status/ {print $2}' | /usr/bin/sort`
    else
        pkglist=`/usr/bin/rpm -qa | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|hip|hcc|hsa|rocm|atmi|comgr|composa|amd-smi|aomp|amdgpu-core|amdgpu-dkms|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rocwmma|rpp|rdc|openmp-' | /usr/bin/sort`
    fi
else
    echo "Remove ROCm packages for release $REV"
    if [ "$pkgtype" = "deb" ]
    then
        pkglist=`/usr/bin/dpkg -l | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|^ii  hip|hcc|hsa|rocm|atmi|^ii  comgr|composa|amd-smi|aomp|amdgpu-core|amdgpu-dkms|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rocwmma|rpp|rdc|openmp-' | /usr/bin/awk '!/Status/ {print $2}' | /bin/grep -E '^[a-zA-Z\-]+[a-zA-Z]'${REV}'|^[a-zA-Z\-]+lib64'${REV} | /usr/bin/sort`
        miopenkernelpkglist=`/usr/bin/dpkg -l | /bin/grep -i -E 'miopenkernel' | /bin/grep -E 'miopenkernels-gfx.+'${REV}'|miopenkernels-gfx.+db'${REV} | /usr/bin/awk '!/Status/ {print $2}' | /usr/bin/sort`
    else
        pkglist=`/usr/bin/rpm -qa | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|hip|hcc|hsa|rocm|atmi|comgr|composa|amd-smi|aomp|amdgpu-core|amdgpu-dkms|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar|rocwmma|rpp|rdc|openmp-' | /bin/grep -E '^[a-zA-Z\-]+[a-zA-Z]'${REV}'|^[a-zA-Z\-]+lib64'${REV} | /usr/bin/sort`
        miopenkernelpkglist=`/usr/bin/rpm -qa | /bin/grep -i -E 'miopenkernel' | /bin/grep -E '^miopenkernels-gfx.+'${REV}'|^miopenkernels-gfx.+db'${REV} | /usr/bin/sort`
    fi
fi

# List the ROCm packages that will be uninstalled
echo "List of packages selected for uninstall: "
echo $pkglist
echo $miopenkernelpkglist

# Prompt user
while true; do
    read -p "Do you want to continue to uninstall above packages [Y/n]?" ans
    case $ans in
        [Yy]* ) echo "Uninstalling...";
	    if [ "$pkgtype" = "deb" ]
	    then
                /usr/bin/apt remove $pkglist $miopenkernelpkglist;
	    elif [ "$pkgtype" = "rpm" ]
	    then
                /usr/bin/yum remove $pkglist $miopenkernelpkglist;
	    else
                /usr/bin/zypper remove $pkglist $miopenkernelpkglist;
                if [ ${REV} = "all" ]
                then
                    /usr/bin/zypper remove amdgpu-core amdgpu-dkms-firmware amdgpu-dkms;
                fi
	    fi
	    break;;
        [Nn]* ) echo "Aborting."; break;;
        * ) echo "Please answer yes or no to continue.";;
    esac
done
