#!/bin/sh
# Copyright (c) 2020 Advanced Micro Devices, Inc. All Rights Reserved.
#
# rocm_techsupport.sh
# This script collects ROCm and system logs on a Debian OS installation.
# It requires 'sudo' supervisor privileges for some log collection
# such as dmidecode, dmesg, lspci -vvv to read capabilities.
# Author: srinivasan.subramanian@amd.com
# Revision: V1.5
# V1.6: In docker, use dmesg
# V1.5: Add error and fault to system log filter
# V1.4: Collect logs from the last 3 boots
#       Add power to grep
# V1.3: Add rocm-bandwidth-test -t to get topology
# V1.2: Add ECC and rask_mask
#       Show ras info, xgmierr
# V1.1: Detect OS type
#       Check paths for lspci, lshw
# V1.0: Initial version
#
echo "=== ROCm TechSupport Log Collection Utility: V1.6 ==="
/bin/date

ret=`/bin/grep -i -E 'debian|ubuntu' /etc/os-release`
if [ $? -ne 0 ]
then
    pkgtype="rpm"
else
    pkgtype="deb"
fi
echo "===== Section: OS Distribution         ==============="
# Print OS type
/bin/uname -a
# OS release
/bin/cat /etc/os-release

# Kernel boot parameters
echo "===== Section: Kernel Boot Parameters  ==============="
/bin/cat /proc/cmdline

# System log related to GPU
echo "===== Section: dmesg GPU/DRM/ATOM/BIOS ==============="
dockerchk=`/bin/grep cpuset /proc/1/cgroup | /usr/bin/awk 'BEGIN {FS=":"} {print $3}'`
if [ "$dockerchk" != "/" ]
then
    echo "Section: Current boot logs"
    /bin/dmesg | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'

elif [ -f /bin/journalctl ]
then
    echo "Section: Current boot logs"
    /bin/journalctl -b | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Previous boot logs"
    /bin/journalctl -b -1 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Second Previous boot logs"
    /bin/journalctl -b -2 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Third Previous boot logs"
    /bin/journalctl -b -3 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
elif [ -f /usr/bin/journalctl ]
then
    /usr/bin/journalctl -b | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Previous boot logs"
    /usr/bin/journalctl -b -1 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Second Previous boot logs"
    /usr/bin/journalctl -b -2 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
    echo "Section: Third Previous boot logs"
    /usr/bin/journalctl -b -3 | /bin/grep -i -E ' Linux v| Command line|power|gpu|drm|error|fault|atom|bios|iommu|ras_mask|ECC|smpboot.*CPU|pcieport.*AER'
else
    echo "ROCmTechSupportNotFound: journalctl/dmesg utility not found!"
fi

# CPU information
echo "===== Section: CPU Information         ==============="
/usr/bin/lscpu

# Memory information
echo "===== Section: Memory Information      ==============="
/usr/bin/lsmem

# Hardware Information
echo "===== Section: Hardware Information    ==============="
if [ -f /usr/bin/lshw ]
then
    /usr/bin/lshw
elif [ -f /usr/sbin/lshw ]
then
    /usr/sbin/lshw
elif [ -f /sbin/lshw ]
then
    /sbin/lshw
else
    echo "Note: Install lshw to get lshw hardware listing information"
    echo "    Ex: sudo apt install lshw "
    echo "ROCmTechSupportNotFound: lshw utility not found!"
fi

# Kernel Modules loaded
echo "===== Section: lsmod loaded module     ==============="
/sbin/lsmod

# amdgpu modinfo
echo "===== Section: amdgpu modinfo          ==============="
/sbin/modinfo amdgpu

# Hardware Topology
echo "===== Section: Hardware Topology       ==============="
if [ -f /usr/bin/lstopo-no-graphics ]
then
    /usr/bin/lstopo-no-graphics
else
    echo "lstopo command not found. Skipping hardware topology information."
    echo "Note: Install hwloc to get lstopo hardware topology information"
    echo "    Ex: sudo apt install hwloc "
fi

# DMIdecode information - BIOS etc
echo "===== Section: dmidecode Information   ==============="
/usr/sbin/dmidecode

# PCI peripheral information
echo "===== Section: lspci verbose output    ==============="
if [ -f /usr/bin/lspci ]
then
    /usr/bin/lspci -vvv
elif [ -f /usr/sbin/lspci ]
then
    /usr/sbin/lspci -vvv
elif [ -f /sbin/lspci ]
then
    /sbin/lspci -vvv
else
    echo "ROCmTechSupportNotFound: lspci utility not found!"
fi

# Print ROCm installed packages
echo "===== Section: ROCm Packages Installed ==============="
if [ "$pkgtype" = "deb" ]
then
    /usr/bin/dpkg -l | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|^hip|hcc|hsa|rocm|atmi|^comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocbl|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar' | /usr/bin/sort
else
    /usr/bin/rpm -qa | /bin/grep -i -E 'ocl-icd|kfdtest|llvm-amd|miopen|half|hip|hcc|hsa|rocm|atmi|comgr|aomp|rock|mivision|migraph|rocprofiler|roctracer|rocblas|hipify|rocsol|rocthr|rocff|rocalu|rocprim|rocrand|rccl|rocspar' | /usr/bin/sort
fi


# Select latest ROCM installed version: only supports 3.1 or newer
ROCM_VERSION=`/bin/ls -d /opt/rocm-* | /usr/bin/sort | /usr/bin/tail -1`
echo "==== Using $ROCM_VERSION to collect ROCm information.==== "

# RBT Topology
echo "===== Section: rocm-bandwidth-test Topology       ==============="
if [ -f $ROCM_VERSION/bin/rocm-bandwidth-test ]
then
    $ROCM_VERSION/bin/rocm-bandwidth-test -t
else
    echo "$ROCM_VERSION/bin/rocm-bandwidth-test command not found. Skipping topology information."
    echo "Note: Install rocb=m-bandwidth-test ROCm package to get topology information"
    echo "    Ex: sudo apt install rocm-bandwidth-test "
fi

# ROCm SMI 
if [ -f $ROCM_VERSION/bin/rocm-smi ]
then
    echo "===== Section: ROCm SMI                ==============="
    $ROCM_VERSION/bin/rocm-smi
fi

# ROCm SMI - FW version
if [ -f $ROCM_VERSION/bin/rocm-smi ]
then
    echo "===== Section: ROCm SMI showhw         ==============="
    $ROCM_VERSION/bin/rocm-smi --showhw
fi

# ROCm SMI - RAS info
if [ -f $ROCM_VERSION/bin/rocm-smi ]
then
    echo "===== Section: ROCm SMI showrasinfo all==============="
    $ROCM_VERSION/bin/rocm-smi --showrasinfo all
fi

# ROCm SMI - xgmierr
if [ -f $ROCM_VERSION/bin/rocm-smi ]
then
    echo "===== Section: ROCm SMI showxgmierr    ==============="
    $ROCM_VERSION/bin/rocm-smi --showxgmierr
fi

# ROCm SMI - FW version clocks etc.
if [ -f $ROCM_VERSION/bin/rocm-smi ]
then
    echo "===== Section: ROCm SMI clocks         ==============="
    $ROCM_VERSION/bin/rocm-smi -cga
fi

# ROCm Agent Information
if [ -f $ROCM_VERSION/bin/rocminfo ]
then
    echo "===== Section: rocminfo                ==============="
    $ROCM_VERSION/bin/rocminfo
fi

# OpenCL Agent Information
if [ -f $ROCM_VERSION/opencl/bin/x86_64/clinfo ]
then
    echo "===== Section: clinfo                  ==============="
    $ROCM_VERSION/opencl/bin/x86_64/clinfo
fi
# path in 3.5
if [ -f $ROCM_VERSION/opencl/bin/clinfo ]
then
    echo "===== Section: clinfo                  ==============="
    $ROCM_VERSION/opencl/bin/clinfo
fi


