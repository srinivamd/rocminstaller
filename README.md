# rocminstaller V1.7 Utility to install ROCm releases directly from ROCm repo

# $ sudo ./rocminstall.py -h
```
./rocminstall.py --help
usage: rocminstall.py [-h] [--rev REVSTRING] [--destdir DESTDIR] [--list]
                      [--repourl REPOURL] [--nokernel]

[V1.6]rocminstall.py: utility to download and install ROCm RPMs for specified
version (requires sudo privilege)

optional arguments:
  -h, --help         show this help message and exit
  --rev REVSTRING    specifies ROCm release repo to use as in
                     http://repo.radeon.com/rocm/{apt, yum zyp}/<REV> Example:
                     --rev 3.3 for ROCm 3.3 repo
                     http://repo.radeon.com/rocm/{apt, yum, zyp}/3.3, or --rev
                     3.1.1 for ROCm 3.1.1 repo
                     http://repo.radeon.com/rocm/{apt, yum, zyp}/3.1.1
  --destdir DESTDIR  specify directory where to download RPM before
                     installation. Default: current directory --destdir /tmp
                     to use /tmp directory
  --list             just list the packages that will be installed -- do not
                     download or install
  --repourl REPOURL  specify ROCm repo URL to use from where to download
                     packages Example: --repourl http://compute-
                     artifactory/build/xyz
  --nokernel         do not install rock kernel packages, for example, used to
                     install ROCm in docker
```
# rocm_techsupport.sh V1.1 Shell Utility for Ubuntu/CentOS/SLES log collection
# $ sudo sh <path_to>/rocm_techsupport.sh 2>&1 | tee <path_to>/rocm_techsupport.logs
```
Example: Run rocm_techsupport.sh in current directory ('.') and save standard output and errors in /tmp/rocm_techsupport.log
# sudo sh ./rocm_techsupport.sh 2>&1 | tee /tmp/rocm_techsupport.log

Compress/Zip the output file and include with reported issue.
```
# rocminstall.py Install ROCm 3.5 Example on CentOS
**$ sudo ./rocminstall.py --list --rev 3.5**
```
testscript]$ sudo ./rocminstall.py --rev 3.5
[sudo] password for master: 
NOTE: Not installing hipify-clang RPM due to packaging issue.
NOTE: Please install hipify-clang RPM manually using: 
NOTE:  sudo rpm -ivh --force hipify-clang3.5.0-11.0.0.x86_64.rpm 
...................................................Loaded plugins: fastestmirror
Examining ./rock-dkms-3.5-30.el7.noarch.rpm: 1:rock-dkms-3.5-30.el7.noarch
Marking ./rock-dkms-3.5-30.el7.noarch.rpm to be installed
Examining ./rock-dkms-firmware-3.5-30.el7.noarch.rpm: 1:rock-dkms-firmware-3.5-30.el7.noarch
Marking ./rock-dkms-firmware-3.5-30.el7.noarch.rpm to be installed
Examining ./aomp-amdgpu-tests3.5.0-11.5-0.x86_64.rpm: aomp-amdgpu-tests3.5.0-11.5-0.x86_64
Marking ./aomp-amdgpu-tests3.5.0-11.5-0.x86_64.rpm to be installed
Examining ./aomp-amdgpu3.5.0-11.5-0.x86_64.rpm: aomp-amdgpu3.5.0-11.5-0.x86_64
Marking ./aomp-amdgpu3.5.0-11.5-0.x86_64.rpm to be installed
Examining ./atmi3.5.0-0.7.11-Linux.rpm: atmi3.5.0-0.7.11-1.x86_64
Marking ./atmi3.5.0-0.7.11-Linux.rpm to be installed
Examining ./comgr3.5.0-1.6.0.143-rocm-rel-3.5-30-e24e8c1-Linux.rpm: comgr3.5.0-1.6.0.143_rocm_rel_3.5_30_e24e8c1-1.x86_64
Marking ./comgr3.5.0-1.6.0.143-rocm-rel-3.5-30-e24e8c1-Linux.rpm to be installed
Examining ./half3.5.0-1.12.0-el7.x86_64.rpm: half3.5.0-1.12.0-1.x86_64
Marking ./half3.5.0-1.12.0-el7.x86_64.rpm to be installed
Examining ./hip-base3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm: hip-base3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64
Marking ./hip-base3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm to be installed
Examining ./hip-doc3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm: hip-doc3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64
Marking ./hip-doc3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm to be installed
Examining ./hip-rocclr3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm: hip-rocclr3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64
Marking ./hip-rocclr3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm to be installed
Examining ./hip-samples3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm: hip-samples3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64
Marking ./hip-samples3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64.rpm to be installed
Examining ./hipblas3.5.0-0.28.0.382-rocm-rel-3.5-30-7d2cb89-el7.x86_64.rpm: hipblas3.5.0-0.28.0.382_rocm_rel_3.5_30_7d2cb89-1.x86_64
Marking ./hipblas3.5.0-0.28.0.382-rocm-rel-3.5-30-7d2cb89-el7.x86_64.rpm to be installed
Examining ./hipcub3.5.0-2.10.1.142-rocm-rel-3.5-30-419b5fb-el7.x86_64.rpm: hipcub3.5.0-2.10.1.142_rocm_rel_3.5_30_419b5fb-1.x86_64
Marking ./hipcub3.5.0-2.10.1.142-rocm-rel-3.5-30-419b5fb-el7.x86_64.rpm to be installed
Examining ./hipsparse3.5.0-1.6.5.282-rocm-rel-3.5-30-9291ddc-el7.x86_64.rpm: hipsparse3.5.0-1.6.5.282_rocm_rel_3.5_30_9291ddc-1.x86_64
Marking ./hipsparse3.5.0-1.6.5.282-rocm-rel-3.5-30-9291ddc-el7.x86_64.rpm to be installed
Examining ./hsa-amd-aqlprofile3.5.0-1.0.0-Linux.rpm: hsa-amd-aqlprofile3.5.0-1.0.0-1.x86_64
Marking ./hsa-amd-aqlprofile3.5.0-1.0.0-Linux.rpm to be installed
Examining ./hsa-ext-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux.rpm: hsa-ext-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64
Marking ./hsa-ext-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux.rpm to be installed
Examining ./hsa-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux.rpm: hsa-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64
Marking ./hsa-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux.rpm to be installed
Examining ./hsakmt-roct-dev3.5.0-1.0.9-347-gd4b224f-Linux.rpm: hsakmt-roct-dev3.5.0-1.0.9_347_gd4b224f-1.x86_64
Marking ./hsakmt-roct-dev3.5.0-1.0.9-347-gd4b224f-Linux.rpm to be installed
Examining ./hsakmt-roct3.5.0-1.0.9-347-gd4b224f.x86_64.rpm: hsakmt-roct3.5.0-1.0.9_347_gd4b224f-1.x86_64
Marking ./hsakmt-roct3.5.0-1.0.9-347-gd4b224f.x86_64.rpm to be installed
Examining ./llvm-amdgpu3.5.0-11.0.dev-1.x86_64.rpm: llvm-amdgpu3.5.0-11.0.dev-1.x86_64
Marking ./llvm-amdgpu3.5.0-11.0.dev-1.x86_64.rpm to be installed
Examining ./migraphx3.5.0-0.6.0.3799-rocm-rel-3.5-30-caee500e-el7.x86_64.rpm: migraphx3.5.0-0.6.0.3799_rocm_rel_3.5_30_caee500e-1.x86_64
Marking ./migraphx3.5.0-0.6.0.3799-rocm-rel-3.5-30-caee500e-el7.x86_64.rpm to be installed
Examining ./miopen-hip3.5.0-2.4.0.8035-rocm-rel-3.5-30-bd4a3307-el7.x86_64.rpm: miopen-hip3.5.0-2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1.x86_64
Marking ./miopen-hip3.5.0-2.4.0.8035-rocm-rel-3.5-30-bd4a3307-el7.x86_64.rpm to be installed
Examining ./miopengemm3.5.0-1.1.6.647-rocm-rel-3.5-30-b51a125-el7.x86_64.rpm: miopengemm3.5.0-1.1.6.647_rocm_rel_3.5_30_b51a125-1.x86_64
Marking ./miopengemm3.5.0-1.1.6.647-rocm-rel-3.5-30-b51a125-el7.x86_64.rpm to be installed
Examining ./rccl3.5.0-2.10.0-112-g250d820-rocm-rel-3.5-30-el7.x86_64.rpm: rccl3.5.0-2.10.0_112_g250d820_rocm_rel_3.5_30-1.x86_64
Marking ./rccl3.5.0-2.10.0-112-g250d820-rocm-rel-3.5-30-el7.x86_64.rpm to be installed
Examining ./rocalution3.5.0-1.9.1.491-rocm-rel-3.5-30-efe39a5-el7.x86_64.rpm: rocalution3.5.0-1.9.1.491_rocm_rel_3.5_30_efe39a5-1.x86_64
Marking ./rocalution3.5.0-1.9.1.491-rocm-rel-3.5-30-efe39a5-el7.x86_64.rpm to be installed
Examining ./rocblas3.5.0-2.22.0.2367-b2cceba2-el7.x86_64.rpm: rocblas3.5.0-2.22.0.2367_b2cceba2-1.x86_64
Marking ./rocblas3.5.0-2.22.0.2367-b2cceba2-el7.x86_64.rpm to be installed
Examining ./rocfft3.5.0-1.0.3.839-rocm-rel-3.5-30-da61945-el7.x86_64.rpm: rocfft3.5.0-1.0.3.839_rocm_rel_3.5_30_da61945-1.x86_64
Marking ./rocfft3.5.0-1.0.3.839-rocm-rel-3.5-30-da61945-el7.x86_64.rpm to be installed
Examining ./rocm-bandwidth-test3.5.0-1.4.0.13-rocm-rel-3.5-30-gf671f73-Linux.rpm: rocm-bandwidth-test3.5.0-1.4.0.13_rocm_rel_3.5_30_gf671f73-1.x86_64
Marking ./rocm-bandwidth-test3.5.0-1.4.0.13-rocm-rel-3.5-30-gf671f73-Linux.rpm to be installed
Examining ./rocm-clang-ocl3.5.0-0.5.0.51-rocm-rel-3.5-30-74b3b81-el7.x86_64.rpm: rocm-clang-ocl3.5.0-0.5.0.51_rocm_rel_3.5_30_74b3b81-1.x86_64
Marking ./rocm-clang-ocl3.5.0-0.5.0.51-rocm-rel-3.5-30-74b3b81-el7.x86_64.rpm to be installed
Examining ./rocm-cmake3.5.0-0.3.0.153-rocm-rel-3.5-30-1d1caa5-el7.x86_64.rpm: rocm-cmake3.5.0-0.3.0.153_rocm_rel_3.5_30_1d1caa5-1.x86_64
Marking ./rocm-cmake3.5.0-0.3.0.153-rocm-rel-3.5-30-1d1caa5-el7.x86_64.rpm to be installed
Examining ./rocm-dbgapi3.5.0-0.21.2-rocm-rel-3.5-30-Linux.rpm: rocm-dbgapi3.5.0-0.21.2_rocm_rel_3.5_30-1.x86_64
Marking ./rocm-dbgapi3.5.0-0.21.2-rocm-rel-3.5-30-Linux.rpm to be installed
Examining ./rocm-debug-agent3.5.0-1.0.0.30500-rocm-rel-3.5-30-Linux.rpm: rocm-debug-agent3.5.0-1.0.0.30500_rocm_rel_3.5_30-1.x86_64
Marking ./rocm-debug-agent3.5.0-1.0.0.30500-rocm-rel-3.5-30-Linux.rpm to be installed
Examining ./rocm-dev3.5.0-3.5.0-30-Linux.rpm: rocm-dev3.5.0-3.5.0_30-1.x86_64
Marking ./rocm-dev3.5.0-3.5.0-30-Linux.rpm to be installed
Examining ./rocm-device-libs3.5.0-1.0.0.585-rocm-rel-3.5-30-e6d1be0-Linux.rpm: rocm-device-libs3.5.0-1.0.0.585_rocm_rel_3.5_30_e6d1be0-1.x86_64
Marking ./rocm-device-libs3.5.0-1.0.0.585-rocm-rel-3.5-30-e6d1be0-Linux.rpm to be installed
Examining ./rocm-dkms3.5.0-3.5.0-30-Linux.rpm: rocm-dkms3.5.0-3.5.0_30-1.x86_64
Marking ./rocm-dkms3.5.0-3.5.0-30-Linux.rpm to be installed
Examining ./rocm-gdb3.5.0-9.1-rocm-rel-3.5-30.x86_64.rpm: rocm-gdb3.5.0-9.1_rocm_rel_3.5_30-1.x86_64
Marking ./rocm-gdb3.5.0-9.1-rocm-rel-3.5-30.x86_64.rpm to be installed
Examining ./rocm-libs3.5.0-3.5.0-30-Linux.rpm: rocm-libs3.5.0-3.5.0_30-1.x86_64
Marking ./rocm-libs3.5.0-3.5.0-30-Linux.rpm to be installed
Examining ./rocm-opencl-dev3.5.0-2.0.20191-db0c16d.x86_64.rpm: rocm-opencl-dev3.5.0-2.0.20191-1.x86_64
Marking ./rocm-opencl-dev3.5.0-2.0.20191-db0c16d.x86_64.rpm to be installed
Examining ./rocm-opencl3.5.0-2.0.20191-db0c16d.x86_64.rpm: rocm-opencl3.5.0-2.0.20191-1.x86_64
Marking ./rocm-opencl3.5.0-2.0.20191-db0c16d.x86_64.rpm to be installed
Examining ./rocm-smi-lib643.5.0-2.3.0.8.rocm-rel-3.5-30-2143bc3.rpm: rocm-smi-lib643.5.0-2.3.0.8.rocm_rel_3.5_30_2143bc3-1.x86_64
Marking ./rocm-smi-lib643.5.0-2.3.0.8.rocm-rel-3.5-30-2143bc3.rpm to be installed
Examining ./rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64.rpm: rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64
Marking ./rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64.rpm to be installed
Examining ./rocm-utils3.5.0-3.5.0-30-Linux.rpm: rocm-utils3.5.0-3.5.0_30-1.x86_64
Marking ./rocm-utils3.5.0-3.5.0-30-Linux.rpm to be installed
Examining ./rocm-validation-suite3.5.0-3.5.30500.rpm: rocm-validation-suite3.5.0-3.5.30500-1.x86_64
Marking ./rocm-validation-suite3.5.0-3.5.30500.rpm to be installed
Examining ./rocminfo3.5.0-1.0.0.0.rocm-rel-3.5-30-5d6be5b.rpm: rocminfo3.5.0-1.30500.0-1.x86_64
Marking ./rocminfo3.5.0-1.0.0.0.rocm-rel-3.5-30-5d6be5b.rpm to be installed
Examining ./rocprim3.5.0-2.10.1.1038-rocm-rel-3.5-30-8e6861f-el7.x86_64.rpm: rocprim3.5.0-2.10.1.1038_rocm_rel_3.5_30_8e6861f-1.x86_64
Marking ./rocprim3.5.0-2.10.1.1038-rocm-rel-3.5-30-8e6861f-el7.x86_64.rpm to be installed
Examining ./rocprofiler-dev3.5.0-1.0.0-Linux.rpm: rocprofiler-dev3.5.0-1.0.0-1.x86_64
Marking ./rocprofiler-dev3.5.0-1.0.0-Linux.rpm to be installed
Examining ./rocrand3.5.0-2.10.1.693-rocm-rel-3.5-30-b465435-Linux.rpm: rocrand3.5.0-2.10.1.693_rocm_rel_3.5_30_b465435-1.x86_64
Marking ./rocrand3.5.0-2.10.1.693-rocm-rel-3.5-30-b465435-Linux.rpm to be installed
Examining ./rocsolver3.5.0-3.5.0.106-rocm-rel-3.5-30-2e45cd8-el7.x86_64.rpm: rocsolver3.5.0-3.5.0.106_rocm_rel_3.5_30_2e45cd8-1.x86_64
Marking ./rocsolver3.5.0-3.5.0.106-rocm-rel-3.5-30-2e45cd8-el7.x86_64.rpm to be installed
Examining ./rocsparse3.5.0-1.12.10.799-rocm-rel-3.5-30-108c40b-el7.x86_64.rpm: rocsparse3.5.0-1.12.10.799_rocm_rel_3.5_30_108c40b-1.x86_64
Marking ./rocsparse3.5.0-1.12.10.799-rocm-rel-3.5-30-108c40b-el7.x86_64.rpm to be installed
Examining ./rocthrust3.5.0-2.10.1.466-rocm-rel-3.5-30-f09291d-el7.x86_64.rpm: rocthrust3.5.0-2.10.1.466_rocm_rel_3.5_30_f09291d-1.x86_64
Marking ./rocthrust3.5.0-2.10.1.466-rocm-rel-3.5-30-f09291d-el7.x86_64.rpm to be installed
Examining ./roctracer-dev3.5.0-1.0.0-Linux.rpm: roctracer-dev3.5.0-1.0.0-1.x86_64
Marking ./roctracer-dev3.5.0-1.0.0-Linux.rpm to be installed
Resolving Dependencies
--> Running transaction check
---> Package aomp-amdgpu-tests3.5.0.x86_64 0:11.5-0 will be installed
---> Package aomp-amdgpu3.5.0.x86_64 0:11.5-0 will be installed
---> Package atmi3.5.0.x86_64 0:0.7.11-1 will be installed
---> Package comgr3.5.0.x86_64 0:1.6.0.143_rocm_rel_3.5_30_e24e8c1-1 will be installed
---> Package half3.5.0.x86_64 0:1.12.0-1 will be installed
---> Package hip-base3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1 will be installed
---> Package hip-doc3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1 will be installed
---> Package hip-rocclr3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1 will be installed
---> Package hip-samples3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1 will be installed
---> Package hipblas3.5.0.x86_64 0:0.28.0.382_rocm_rel_3.5_30_7d2cb89-1 will be installed
---> Package hipcub3.5.0.x86_64 0:2.10.1.142_rocm_rel_3.5_30_419b5fb-1 will be installed
---> Package hipsparse3.5.0.x86_64 0:1.6.5.282_rocm_rel_3.5_30_9291ddc-1 will be installed
---> Package hsa-amd-aqlprofile3.5.0.x86_64 0:1.0.0-1 will be installed
---> Package hsa-ext-rocr-dev3.5.0.x86_64 0:1.1.30500.0_rocm_rel_3.5_30_def83d8a-1 will be installed
---> Package hsa-rocr-dev3.5.0.x86_64 0:1.1.30500.0_rocm_rel_3.5_30_def83d8a-1 will be installed
---> Package hsakmt-roct-dev3.5.0.x86_64 0:1.0.9_347_gd4b224f-1 will be installed
---> Package hsakmt-roct3.5.0.x86_64 0:1.0.9_347_gd4b224f-1 will be installed
---> Package llvm-amdgpu3.5.0.x86_64 0:11.0.dev-1 will be installed
---> Package migraphx3.5.0.x86_64 0:0.6.0.3799_rocm_rel_3.5_30_caee500e-1 will be installed
---> Package miopen-hip3.5.0.x86_64 0:2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1 will be installed
---> Package miopengemm3.5.0.x86_64 0:1.1.6.647_rocm_rel_3.5_30_b51a125-1 will be installed
---> Package rccl3.5.0.x86_64 0:2.10.0_112_g250d820_rocm_rel_3.5_30-1 will be installed
---> Package rocalution3.5.0.x86_64 0:1.9.1.491_rocm_rel_3.5_30_efe39a5-1 will be installed
---> Package rocblas3.5.0.x86_64 0:2.22.0.2367_b2cceba2-1 will be installed
---> Package rocfft3.5.0.x86_64 0:1.0.3.839_rocm_rel_3.5_30_da61945-1 will be installed
---> Package rock-dkms.noarch 1:3.5-30.el7 will be installed
---> Package rock-dkms-firmware.noarch 1:3.5-30.el7 will be installed
---> Package rocm-bandwidth-test3.5.0.x86_64 0:1.4.0.13_rocm_rel_3.5_30_gf671f73-1 will be installed
---> Package rocm-clang-ocl3.5.0.x86_64 0:0.5.0.51_rocm_rel_3.5_30_74b3b81-1 will be installed
---> Package rocm-cmake3.5.0.x86_64 0:0.3.0.153_rocm_rel_3.5_30_1d1caa5-1 will be installed
---> Package rocm-dbgapi3.5.0.x86_64 0:0.21.2_rocm_rel_3.5_30-1 will be installed
---> Package rocm-debug-agent3.5.0.x86_64 0:1.0.0.30500_rocm_rel_3.5_30-1 will be installed
---> Package rocm-dev3.5.0.x86_64 0:3.5.0_30-1 will be installed
---> Package rocm-device-libs3.5.0.x86_64 0:1.0.0.585_rocm_rel_3.5_30_e6d1be0-1 will be installed
---> Package rocm-dkms3.5.0.x86_64 0:3.5.0_30-1 will be installed
---> Package rocm-gdb3.5.0.x86_64 0:9.1_rocm_rel_3.5_30-1 will be installed
---> Package rocm-libs3.5.0.x86_64 0:3.5.0_30-1 will be installed
---> Package rocm-opencl-dev3.5.0.x86_64 0:2.0.20191-1 will be installed
---> Package rocm-opencl3.5.0.x86_64 0:2.0.20191-1 will be installed
---> Package rocm-smi-lib643.5.0.x86_64 0:2.3.0.8.rocm_rel_3.5_30_2143bc3-1 will be installed
---> Package rocm-smi3.5.0.x86_64 0:1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1 will be installed
---> Package rocm-utils3.5.0.x86_64 0:3.5.0_30-1 will be installed
---> Package rocm-validation-suite3.5.0.x86_64 0:3.5.30500-1 will be installed
---> Package rocminfo3.5.0.x86_64 0:1.30500.0-1 will be installed
---> Package rocprim3.5.0.x86_64 0:2.10.1.1038_rocm_rel_3.5_30_8e6861f-1 will be installed
---> Package rocprofiler-dev3.5.0.x86_64 0:1.0.0-1 will be installed
---> Package rocrand3.5.0.x86_64 0:2.10.1.693_rocm_rel_3.5_30_b465435-1 will be installed
---> Package rocsolver3.5.0.x86_64 0:3.5.0.106_rocm_rel_3.5_30_2e45cd8-1 will be installed
---> Package rocsparse3.5.0.x86_64 0:1.12.10.799_rocm_rel_3.5_30_108c40b-1 will be installed
---> Package rocthrust3.5.0.x86_64 0:2.10.1.466_rocm_rel_3.5_30_f09291d-1 will be installed
---> Package roctracer-dev3.5.0.x86_64 0:1.0.0-1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==============================================================================================================================
 Package              Arch   Version                               Repository                                            Size
==============================================================================================================================
Installing:
 aomp-amdgpu-tests3.5.0
                      x86_64 11.5-0                                /aomp-amdgpu-tests3.5.0-11.5-0.x86_64                173 k
 aomp-amdgpu3.5.0     x86_64 11.5-0                                /aomp-amdgpu3.5.0-11.5-0.x86_64                      2.4 G
 atmi3.5.0            x86_64 0.7.11-1                              /atmi3.5.0-0.7.11-Linux                              3.9 M
 comgr3.5.0           x86_64 1.6.0.143_rocm_rel_3.5_30_e24e8c1-1   /comgr3.5.0-1.6.0.143-rocm-rel-3.5-30-e24e8c1-Linux  117 M
 half3.5.0            x86_64 1.12.0-1                              /half3.5.0-1.12.0-el7.x86_64                         146 k
 hip-base3.5.0        x86_64 3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1
                                                                   /hip-base3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64
                                                                                                                        2.2 M
 hip-doc3.5.0         x86_64 3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1
                                                                   /hip-doc3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64
                                                                                                                        8.9 M
 hip-rocclr3.5.0      x86_64 3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1
                                                                   /hip-rocclr3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64
                                                                                                                        2.7 M
 hip-samples3.5.0     x86_64 3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1
                                                                   /hip-samples3.5.0-3.5.20214.5355-rocm-rel-3.5-30-a2917cdc.x86_64
                                                                                                                        355 k
 hipblas3.5.0         x86_64 0.28.0.382_rocm_rel_3.5_30_7d2cb89-1  /hipblas3.5.0-0.28.0.382-rocm-rel-3.5-30-7d2cb89-el7.x86_64
                                                                                                                        648 k
 hipcub3.5.0          x86_64 2.10.1.142_rocm_rel_3.5_30_419b5fb-1  /hipcub3.5.0-2.10.1.142-rocm-rel-3.5-30-419b5fb-el7.x86_64
                                                                                                                        327 k
 hipsparse3.5.0       x86_64 1.6.5.282_rocm_rel_3.5_30_9291ddc-1   /hipsparse3.5.0-1.6.5.282-rocm-rel-3.5-30-9291ddc-el7.x86_64
                                                                                                                        305 k
 hsa-amd-aqlprofile3.5.0
                      x86_64 1.0.0-1                               /hsa-amd-aqlprofile3.5.0-1.0.0-Linux                 239 k
 hsa-ext-rocr-dev3.5.0
                      x86_64 1.1.30500.0_rocm_rel_3.5_30_def83d8a-1
                                                                   /hsa-ext-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux
                                                                                                                        1.3 M
 hsa-rocr-dev3.5.0    x86_64 1.1.30500.0_rocm_rel_3.5_30_def83d8a-1
                                                                   /hsa-rocr-dev3.5.0-1.1.30500.0-rocm-rel-3.5-30-def83d8a-Linux
                                                                                                                        1.5 M
 hsakmt-roct-dev3.5.0 x86_64 1.0.9_347_gd4b224f-1                  /hsakmt-roct-dev3.5.0-1.0.9-347-gd4b224f-Linux        92 k
 hsakmt-roct3.5.0     x86_64 1.0.9_347_gd4b224f-1                  /hsakmt-roct3.5.0-1.0.9-347-gd4b224f.x86_64          180 k
 llvm-amdgpu3.5.0     x86_64 11.0.dev-1                            /llvm-amdgpu3.5.0-11.0.dev-1.x86_64                  2.1 G
 migraphx3.5.0        x86_64 0.6.0.3799_rocm_rel_3.5_30_caee500e-1 /migraphx3.5.0-0.6.0.3799-rocm-rel-3.5-30-caee500e-el7.x86_64
                                                                                                                        204 M
 miopen-hip3.5.0      x86_64 2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1 /miopen-hip3.5.0-2.4.0.8035-rocm-rel-3.5-30-bd4a3307-el7.x86_64
                                                                                                                        215 M
 miopengemm3.5.0      x86_64 1.1.6.647_rocm_rel_3.5_30_b51a125-1   /miopengemm3.5.0-1.1.6.647-rocm-rel-3.5-30-b51a125-el7.x86_64
                                                                                                                        3.5 M
 rccl3.5.0            x86_64 2.10.0_112_g250d820_rocm_rel_3.5_30-1 /rccl3.5.0-2.10.0-112-g250d820-rocm-rel-3.5-30-el7.x86_64
                                                                                                                        102 M
 rocalution3.5.0      x86_64 1.9.1.491_rocm_rel_3.5_30_efe39a5-1   /rocalution3.5.0-1.9.1.491-rocm-rel-3.5-30-efe39a5-el7.x86_64
                                                                                                                         16 M
 rocblas3.5.0         x86_64 2.22.0.2367_b2cceba2-1                /rocblas3.5.0-2.22.0.2367-b2cceba2-el7.x86_64        505 M
 rocfft3.5.0          x86_64 1.0.3.839_rocm_rel_3.5_30_da61945-1   /rocfft3.5.0-1.0.3.839-rocm-rel-3.5-30-da61945-el7.x86_64
                                                                                                                        488 M
 rock-dkms            noarch 1:3.5-30.el7                          /rock-dkms-3.5-30.el7.noarch                         169 M
 rock-dkms-firmware   noarch 1:3.5-30.el7                          /rock-dkms-firmware-3.5-30.el7.noarch                 35 M
 rocm-bandwidth-test3.5.0
                      x86_64 1.4.0.13_rocm_rel_3.5_30_gf671f73-1   /rocm-bandwidth-test3.5.0-1.4.0.13-rocm-rel-3.5-30-gf671f73-Linux
                                                                                                                        243 k
 rocm-clang-ocl3.5.0  x86_64 0.5.0.51_rocm_rel_3.5_30_74b3b81-1    /rocm-clang-ocl3.5.0-0.5.0.51-rocm-rel-3.5-30-74b3b81-el7.x86_64
                                                                                                                        2.1 k
 rocm-cmake3.5.0      x86_64 0.3.0.153_rocm_rel_3.5_30_1d1caa5-1   /rocm-cmake3.5.0-0.3.0.153-rocm-rel-3.5-30-1d1caa5-el7.x86_64
                                                                                                                         39 k
 rocm-dbgapi3.5.0     x86_64 0.21.2_rocm_rel_3.5_30-1              /rocm-dbgapi3.5.0-0.21.2-rocm-rel-3.5-30-Linux       1.3 M
 rocm-debug-agent3.5.0
                      x86_64 1.0.0.30500_rocm_rel_3.5_30-1         /rocm-debug-agent3.5.0-1.0.0.30500-rocm-rel-3.5-30-Linux
                                                                                                                        2.8 M
 rocm-dev3.5.0        x86_64 3.5.0_30-1                            /rocm-dev3.5.0-3.5.0-30-Linux                        8.0  
 rocm-device-libs3.5.0
                      x86_64 1.0.0.585_rocm_rel_3.5_30_e6d1be0-1   /rocm-device-libs3.5.0-1.0.0.585-rocm-rel-3.5-30-e6d1be0-Linux
                                                                                                                        3.1 M
 rocm-dkms3.5.0       x86_64 3.5.0_30-1                            /rocm-dkms3.5.0-3.5.0-30-Linux                       8.0  
 rocm-gdb3.5.0        x86_64 9.1_rocm_rel_3.5_30-1                 /rocm-gdb3.5.0-9.1-rocm-rel-3.5-30.x86_64             15 M
 rocm-libs3.5.0       x86_64 3.5.0_30-1                            /rocm-libs3.5.0-3.5.0-30-Linux                       8.0  
 rocm-opencl-dev3.5.0 x86_64 2.0.20191-1                           /rocm-opencl-dev3.5.0-2.0.20191-db0c16d.x86_64       847 k
 rocm-opencl3.5.0     x86_64 2.0.20191-1                           /rocm-opencl3.5.0-2.0.20191-db0c16d.x86_64           1.7 M
 rocm-smi-lib643.5.0  x86_64 2.3.0.8.rocm_rel_3.5_30_2143bc3-1     /rocm-smi-lib643.5.0-2.3.0.8.rocm-rel-3.5-30-2143bc3 653 k
 rocm-smi3.5.0        x86_64 1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1  /rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64
                                                                                                                        121 k
 rocm-utils3.5.0      x86_64 3.5.0_30-1                            /rocm-utils3.5.0-3.5.0-30-Linux                      8.0  
 rocm-validation-suite3.5.0
                      x86_64 3.5.30500-1                           /rocm-validation-suite3.5.0-3.5.30500                 25 M
 rocminfo3.5.0        x86_64 1.30500.0-1                           /rocminfo3.5.0-1.0.0.0.rocm-rel-3.5-30-5d6be5b        66 k
 rocprim3.5.0         x86_64 2.10.1.1038_rocm_rel_3.5_30_8e6861f-1 /rocprim3.5.0-2.10.1.1038-rocm-rel-3.5-30-8e6861f-el7.x86_64
                                                                                                                        1.3 M
 rocprofiler-dev3.5.0 x86_64 1.0.0-1                               /rocprofiler-dev3.5.0-1.0.0-Linux                    687 k
 rocrand3.5.0         x86_64 2.10.1.693_rocm_rel_3.5_30_b465435-1  /rocrand3.5.0-2.10.1.693-rocm-rel-3.5-30-b465435-Linux
                                                                                                                         15 M
 rocsolver3.5.0       x86_64 3.5.0.106_rocm_rel_3.5_30_2e45cd8-1   /rocsolver3.5.0-3.5.0.106-rocm-rel-3.5-30-2e45cd8-el7.x86_64
                                                                                                                        7.1 M
 rocsparse3.5.0       x86_64 1.12.10.799_rocm_rel_3.5_30_108c40b-1 /rocsparse3.5.0-1.12.10.799-rocm-rel-3.5-30-108c40b-el7.x86_64
                                                                                                                         33 M
 rocthrust3.5.0       x86_64 2.10.1.466_rocm_rel_3.5_30_f09291d-1  /rocthrust3.5.0-2.10.1.466-rocm-rel-3.5-30-f09291d-el7.x86_64
                                                                                                                        6.4 M
 roctracer-dev3.5.0   x86_64 1.0.0-1                               /roctracer-dev3.5.0-1.0.0-Linux                      2.2 M

Transaction Summary
==============================================================================================================================
Install  51 Packages

Total size: 6.5 G
Installed size: 6.5 G
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
Warning: RPMDB altered outside of yum.
** Found 1 pre-existing rpmdb problem(s), 'yum check' output follows:
rocm-dkms3.3.0-3.3.0_19-1.x86_64 has missing requires of rock-dkms
  Installing : hsakmt-roct3.5.0-1.0.9_347_gd4b224f-1.x86_64                                                              1/51 
  Installing : hsa-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64                                           2/51 
  Installing : comgr3.5.0-1.6.0.143_rocm_rel_3.5_30_e24e8c1-1.x86_64                                                     3/51 
  Installing : rocblas3.5.0-2.22.0.2367_b2cceba2-1.x86_64                                                                4/51 
  Installing : hsa-ext-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64                                       5/51 
  Installing : hip-base3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                            6/51 
  Installing : rocm-dbgapi3.5.0-0.21.2_rocm_rel_3.5_30-1.x86_64                                                          7/51 
  Installing : llvm-amdgpu3.5.0-11.0.dev-1.x86_64                                                                        8/51 
  Installing : rocm-gdb3.5.0-9.1_rocm_rel_3.5_30-1.x86_64                                                                9/51 
  Installing : hip-doc3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                            10/51 
  Installing : rocm-opencl3.5.0-2.0.20191-1.x86_64                                                                      11/51 
  Installing : rocm-opencl-dev3.5.0-2.0.20191-1.x86_64                                                                  12/51 
  Installing : rocm-clang-ocl3.5.0-0.5.0.51_rocm_rel_3.5_30_74b3b81-1.x86_64                                            13/51 
  Installing : hipblas3.5.0-0.28.0.382_rocm_rel_3.5_30_7d2cb89-1.x86_64                                                 14/51 
  Installing : roctracer-dev3.5.0-1.0.0-1.x86_64                                                                        15/51 
  Installing : hsa-amd-aqlprofile3.5.0-1.0.0-1.x86_64                                                                   16/51 
  Installing : rocprofiler-dev3.5.0-1.0.0-1.x86_64                                                                      17/51 
  Installing : rocminfo3.5.0-1.30500.0-1.x86_64                                                                         18/51 
  Installing : rocm-utils3.5.0-3.5.0_30-1.x86_64                                                                        19/51 
  Installing : hip-rocclr3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                         20/51 
  Installing : hip-samples3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                        21/51 
  Installing : miopen-hip3.5.0-2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1.x86_64                                             22/51 
  Installing : rocm-debug-agent3.5.0-1.0.0.30500_rocm_rel_3.5_30-1.x86_64                                               23/51 
  Installing : hsakmt-roct-dev3.5.0-1.0.9_347_gd4b224f-1.x86_64                                                         24/51 
  Installing : rocm-cmake3.5.0-0.3.0.153_rocm_rel_3.5_30_1d1caa5-1.x86_64                                               25/51 
  Installing : rocsolver3.5.0-3.5.0.106_rocm_rel_3.5_30_2e45cd8-1.x86_64                                                26/51 
  Installing : rocrand3.5.0-2.10.1.693_rocm_rel_3.5_30_b465435-1.x86_64                                                 27/51 
  Installing : 1:rock-dkms-firmware-3.5-30.el7.noarch                                                                   28/51 
  Installing : 1:rock-dkms-3.5-30.el7.noarch                                                                            29/51 
Loading new amdgpu-3.5-30.el7 DKMS files...
Building for 3.10.0-1062.12.1.el7.x86_64
Building initial module for 3.10.0-1062.12.1.el7.x86_64
Done.
Forcing installation of amdgpu

amdgpu.ko.xz:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/3.10.0-1062.12.1.el7.x86_64/extra/

amdttm.ko.xz:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/3.10.0-1062.12.1.el7.x86_64/extra/

amdkcl.ko.xz:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/3.10.0-1062.12.1.el7.x86_64/extra/

amd-sched.ko.xz:
Running module version sanity check.
 - Original module
   - No original module exists within this kernel
 - Installation
   - Installing to /lib/modules/3.10.0-1062.12.1.el7.x86_64/extra/
Adding any weak-modules
[...]

depmod....

Backing up initramfs-3.10.0-1062.12.1.el7.x86_64.img to /boot/initramfs-3.10.0-1062.12.1.el7.x86_64.img.old-dkms
Making new initramfs-3.10.0-1062.12.1.el7.x86_64.img
(If next boot fails, revert to initramfs-3.10.0-1062.12.1.el7.x86_64.img.old-dkms image)
dracut...............

DKMS: install completed.
  Installing : rocm-smi-lib643.5.0-2.3.0.8.rocm_rel_3.5_30_2143bc3-1.x86_64                                             30/51 
  Installing : half3.5.0-1.12.0-1.x86_64                                                                                31/51 
  Installing : rocm-device-libs3.5.0-1.0.0.585_rocm_rel_3.5_30_e6d1be0-1.x86_64                                         32/51 
  Installing : rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64                                                33/51 
  Installing : rocm-dev3.5.0-3.5.0_30-1.x86_64                                                                          34/51 
  Installing : rocprim3.5.0-2.10.1.1038_rocm_rel_3.5_30_8e6861f-1.x86_64                                                35/51 
  Installing : rocsparse3.5.0-1.12.10.799_rocm_rel_3.5_30_108c40b-1.x86_64                                              36/51 
  Installing : hipsparse3.5.0-1.6.5.282_rocm_rel_3.5_30_9291ddc-1.x86_64                                                37/51 
  Installing : rocalution3.5.0-1.9.1.491_rocm_rel_3.5_30_efe39a5-1.x86_64                                               38/51 
  Installing : hipcub3.5.0-2.10.1.142_rocm_rel_3.5_30_419b5fb-1.x86_64                                                  39/51 
  Installing : rocthrust3.5.0-2.10.1.466_rocm_rel_3.5_30_f09291d-1.x86_64                                               40/51 
  Installing : rocfft3.5.0-1.0.3.839_rocm_rel_3.5_30_da61945-1.x86_64                                                   41/51 
  Installing : rocm-libs3.5.0-3.5.0_30-1.x86_64                                                                         42/51 
  Installing : rocm-dkms3.5.0-3.5.0_30-1.x86_64                                                                         43/51 
  Installing : rccl3.5.0-2.10.0_112_g250d820_rocm_rel_3.5_30-1.x86_64                                                   44/51 
  Installing : migraphx3.5.0-0.6.0.3799_rocm_rel_3.5_30_caee500e-1.x86_64                                               45/51 
  Installing : aomp-amdgpu3.5.0-11.5-0.x86_64                                                                           46/51 
  Installing : atmi3.5.0-0.7.11-1.x86_64                                                                                47/51 
  Installing : rocm-bandwidth-test3.5.0-1.4.0.13_rocm_rel_3.5_30_gf671f73-1.x86_64                                      48/51 
  Installing : aomp-amdgpu-tests3.5.0-11.5-0.x86_64                                                                     49/51 
  Installing : miopengemm3.5.0-1.1.6.647_rocm_rel_3.5_30_b51a125-1.x86_64                                               50/51 
  Installing : rocm-validation-suite3.5.0-3.5.30500-1.x86_64                                                            51/51 
  Verifying  : roctracer-dev3.5.0-1.0.0-1.x86_64                                                                         1/51 
  Verifying  : rocm-libs3.5.0-3.5.0_30-1.x86_64                                                                          2/51 
  Verifying  : rocm-dkms3.5.0-3.5.0_30-1.x86_64                                                                          3/51 
  Verifying  : rocfft3.5.0-1.0.3.839_rocm_rel_3.5_30_da61945-1.x86_64                                                    4/51 
  Verifying  : migraphx3.5.0-0.6.0.3799_rocm_rel_3.5_30_caee500e-1.x86_64                                                5/51 
  Verifying  : rccl3.5.0-2.10.0_112_g250d820_rocm_rel_3.5_30-1.x86_64                                                    6/51 
  Verifying  : hsa-amd-aqlprofile3.5.0-1.0.0-1.x86_64                                                                    7/51 
  Verifying  : hsa-ext-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64                                       8/51 
  Verifying  : rocm-smi3.5.0-1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1.x86_64                                                 9/51 
  Verifying  : rocm-validation-suite3.5.0-3.5.30500-1.x86_64                                                            10/51 
  Verifying  : hsakmt-roct3.5.0-1.0.9_347_gd4b224f-1.x86_64                                                             11/51 
  Verifying  : hip-base3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                           12/51 
  Verifying  : miopengemm3.5.0-1.1.6.647_rocm_rel_3.5_30_b51a125-1.x86_64                                               13/51 
  Verifying  : rocm-dbgapi3.5.0-0.21.2_rocm_rel_3.5_30-1.x86_64                                                         14/51 
  Verifying  : hip-doc3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                            15/51 
  Verifying  : rocm-opencl-dev3.5.0-2.0.20191-1.x86_64                                                                  16/51 
  Verifying  : rocm-dev3.5.0-3.5.0_30-1.x86_64                                                                          17/51 
  Verifying  : hipcub3.5.0-2.10.1.142_rocm_rel_3.5_30_419b5fb-1.x86_64                                                  18/51 
  Verifying  : rocm-device-libs3.5.0-1.0.0.585_rocm_rel_3.5_30_e6d1be0-1.x86_64                                         19/51 
  Verifying  : rocprim3.5.0-2.10.1.1038_rocm_rel_3.5_30_8e6861f-1.x86_64                                                20/51 
  Verifying  : half3.5.0-1.12.0-1.x86_64                                                                                21/51 
  Verifying  : rocm-smi-lib643.5.0-2.3.0.8.rocm_rel_3.5_30_2143bc3-1.x86_64                                             22/51 
  Verifying  : hip-samples3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                        23/51 
  Verifying  : 1:rock-dkms-firmware-3.5-30.el7.noarch                                                                   24/51 
  Verifying  : 1:rock-dkms-3.5-30.el7.noarch                                                                            25/51 
  Verifying  : rocprofiler-dev3.5.0-1.0.0-1.x86_64                                                                      26/51 
  Verifying  : rocminfo3.5.0-1.30500.0-1.x86_64                                                                         27/51 
  Verifying  : hsa-rocr-dev3.5.0-1.1.30500.0_rocm_rel_3.5_30_def83d8a-1.x86_64                                          28/51 
  Verifying  : hip-rocclr3.5.0-3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1.x86_64                                         29/51 
  Verifying  : miopen-hip3.5.0-2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1.x86_64                                             30/51 
  Verifying  : rocthrust3.5.0-2.10.1.466_rocm_rel_3.5_30_f09291d-1.x86_64                                               31/51 
  Verifying  : hipsparse3.5.0-1.6.5.282_rocm_rel_3.5_30_9291ddc-1.x86_64                                                32/51 
  Verifying  : llvm-amdgpu3.5.0-11.0.dev-1.x86_64                                                                       33/51 
  Verifying  : aomp-amdgpu3.5.0-11.5-0.x86_64                                                                           34/51 
  Verifying  : comgr3.5.0-1.6.0.143_rocm_rel_3.5_30_e24e8c1-1.x86_64                                                    35/51 
  Verifying  : rocsparse3.5.0-1.12.10.799_rocm_rel_3.5_30_108c40b-1.x86_64                                              36/51 
  Verifying  : rocalution3.5.0-1.9.1.491_rocm_rel_3.5_30_efe39a5-1.x86_64                                               37/51 
  Verifying  : rocrand3.5.0-2.10.1.693_rocm_rel_3.5_30_b465435-1.x86_64                                                 38/51 
  Verifying  : rocm-bandwidth-test3.5.0-1.4.0.13_rocm_rel_3.5_30_gf671f73-1.x86_64                                      39/51 
  Verifying  : rocm-utils3.5.0-3.5.0_30-1.x86_64                                                                        40/51 
  Verifying  : rocsolver3.5.0-3.5.0.106_rocm_rel_3.5_30_2e45cd8-1.x86_64                                                41/51 
  Verifying  : rocm-gdb3.5.0-9.1_rocm_rel_3.5_30-1.x86_64                                                               42/51 
  Verifying  : rocblas3.5.0-2.22.0.2367_b2cceba2-1.x86_64                                                               43/51 
  Verifying  : rocm-debug-agent3.5.0-1.0.0.30500_rocm_rel_3.5_30-1.x86_64                                               44/51 
  Verifying  : rocm-opencl3.5.0-2.0.20191-1.x86_64                                                                      45/51 
  Verifying  : rocm-clang-ocl3.5.0-0.5.0.51_rocm_rel_3.5_30_74b3b81-1.x86_64                                            46/51 
  Verifying  : aomp-amdgpu-tests3.5.0-11.5-0.x86_64                                                                     47/51 
  Verifying  : hipblas3.5.0-0.28.0.382_rocm_rel_3.5_30_7d2cb89-1.x86_64                                                 48/51 
  Verifying  : rocm-cmake3.5.0-0.3.0.153_rocm_rel_3.5_30_1d1caa5-1.x86_64                                               49/51 
  Verifying  : atmi3.5.0-0.7.11-1.x86_64                                                                                50/51 
  Verifying  : hsakmt-roct-dev3.5.0-1.0.9_347_gd4b224f-1.x86_64                                                         51/51 

Installed:
  aomp-amdgpu-tests3.5.0.x86_64 0:11.5-0                                                                                      
  aomp-amdgpu3.5.0.x86_64 0:11.5-0                                                                                            
  atmi3.5.0.x86_64 0:0.7.11-1                                                                                                 
  comgr3.5.0.x86_64 0:1.6.0.143_rocm_rel_3.5_30_e24e8c1-1                                                                     
  half3.5.0.x86_64 0:1.12.0-1                                                                                                 
  hip-base3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1                                                            
  hip-doc3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1                                                             
  hip-rocclr3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1                                                          
  hip-samples3.5.0.x86_64 0:3.5.20214.5355_rocm_rel_3.5_30_a2917cdc-1                                                         
  hipblas3.5.0.x86_64 0:0.28.0.382_rocm_rel_3.5_30_7d2cb89-1                                                                  
  hipcub3.5.0.x86_64 0:2.10.1.142_rocm_rel_3.5_30_419b5fb-1                                                                   
  hipsparse3.5.0.x86_64 0:1.6.5.282_rocm_rel_3.5_30_9291ddc-1                                                                 
  hsa-amd-aqlprofile3.5.0.x86_64 0:1.0.0-1                                                                                    
  hsa-ext-rocr-dev3.5.0.x86_64 0:1.1.30500.0_rocm_rel_3.5_30_def83d8a-1                                                       
  hsa-rocr-dev3.5.0.x86_64 0:1.1.30500.0_rocm_rel_3.5_30_def83d8a-1                                                           
  hsakmt-roct-dev3.5.0.x86_64 0:1.0.9_347_gd4b224f-1                                                                          
  hsakmt-roct3.5.0.x86_64 0:1.0.9_347_gd4b224f-1                                                                              
  llvm-amdgpu3.5.0.x86_64 0:11.0.dev-1                                                                                        
  migraphx3.5.0.x86_64 0:0.6.0.3799_rocm_rel_3.5_30_caee500e-1                                                                
  miopen-hip3.5.0.x86_64 0:2.4.0.8035_rocm_rel_3.5_30_bd4a3307-1                                                              
  miopengemm3.5.0.x86_64 0:1.1.6.647_rocm_rel_3.5_30_b51a125-1                                                                
  rccl3.5.0.x86_64 0:2.10.0_112_g250d820_rocm_rel_3.5_30-1                                                                    
  rocalution3.5.0.x86_64 0:1.9.1.491_rocm_rel_3.5_30_efe39a5-1                                                                
  rocblas3.5.0.x86_64 0:2.22.0.2367_b2cceba2-1                                                                                
  rocfft3.5.0.x86_64 0:1.0.3.839_rocm_rel_3.5_30_da61945-1                                                                    
  rock-dkms.noarch 1:3.5-30.el7                                                                                               
  rock-dkms-firmware.noarch 1:3.5-30.el7                                                                                      
  rocm-bandwidth-test3.5.0.x86_64 0:1.4.0.13_rocm_rel_3.5_30_gf671f73-1                                                       
  rocm-clang-ocl3.5.0.x86_64 0:0.5.0.51_rocm_rel_3.5_30_74b3b81-1                                                             
  rocm-cmake3.5.0.x86_64 0:0.3.0.153_rocm_rel_3.5_30_1d1caa5-1                                                                
  rocm-dbgapi3.5.0.x86_64 0:0.21.2_rocm_rel_3.5_30-1                                                                          
  rocm-debug-agent3.5.0.x86_64 0:1.0.0.30500_rocm_rel_3.5_30-1                                                                
  rocm-dev3.5.0.x86_64 0:3.5.0_30-1                                                                                           
  rocm-device-libs3.5.0.x86_64 0:1.0.0.585_rocm_rel_3.5_30_e6d1be0-1                                                          
  rocm-dkms3.5.0.x86_64 0:3.5.0_30-1                                                                                          
  rocm-gdb3.5.0.x86_64 0:9.1_rocm_rel_3.5_30-1                                                                                
  rocm-libs3.5.0.x86_64 0:3.5.0_30-1                                                                                          
  rocm-opencl-dev3.5.0.x86_64 0:2.0.20191-1                                                                                   
  rocm-opencl3.5.0.x86_64 0:2.0.20191-1                                                                                       
  rocm-smi-lib643.5.0.x86_64 0:2.3.0.8.rocm_rel_3.5_30_2143bc3-1                                                              
  rocm-smi3.5.0.x86_64 0:1.0.0_201_rocm_rel_3.5_30_gcdfbef4-1                                                                 
  rocm-utils3.5.0.x86_64 0:3.5.0_30-1                                                                                         
  rocm-validation-suite3.5.0.x86_64 0:3.5.30500-1                                                                             
  rocminfo3.5.0.x86_64 0:1.30500.0-1                                                                                          
  rocprim3.5.0.x86_64 0:2.10.1.1038_rocm_rel_3.5_30_8e6861f-1                                                                 
  rocprofiler-dev3.5.0.x86_64 0:1.0.0-1                                                                                       
  rocrand3.5.0.x86_64 0:2.10.1.693_rocm_rel_3.5_30_b465435-1                                                                  
  rocsolver3.5.0.x86_64 0:3.5.0.106_rocm_rel_3.5_30_2e45cd8-1                                                                 
  rocsparse3.5.0.x86_64 0:1.12.10.799_rocm_rel_3.5_30_108c40b-1                                                               
  rocthrust3.5.0.x86_64 0:2.10.1.466_rocm_rel_3.5_30_f09291d-1                                                                
  roctracer-dev3.5.0.x86_64 0:1.0.0-1                                                                                         

Complete!
```

# rocminstall.py Example Output on CentOS system
## To List ROCm 3.3 packages available for installation (will skip rock-dkms if one already installed)
**$ ./rocminstall.py --list --rev 3.3**
```
 ./rocminstall.py --list --rev 3.3
rock-dkms-3.3-19.el7.noarch

 Skipping rock-dkms: a version is already installed.
 To install rock-dkms package, please remove installed rock-dkms first. Reboot may be required. 
List of packages selected:



MIGraphX3.3.0-0.6.0.3793_rocm_rel_3.3_19_d1e945da-1.x86_64.rpm
MIOpen-HIP3.3.0-2.3.0.7730_rocm_rel_3.3_19_ef17912f-1.x86_64.rpm
aomp-amdgpu-tests3.3.0-0.7-6.x86_64.rpm
aomp-amdgpu3.3.0-0.7-6.x86_64.rpm
atmi3.3.0-0.7.11-1.x86_64.rpm
comgr3.3.0-1.6.0.124_rocm_rel_3.3_19_7ac2e34-1.x86_64.rpm
half3.3.0-1.12.0-1.x86_64.rpm
hcc3.3.0-3.1.20114-1.x86_64.rpm
hip-base3.3.0-3.3.20126.4629_rocm_rel_3.3_19_2dbba46b-1.x86_64.rpm
hip-doc3.3.0-3.3.20126.4629_rocm_rel_3.3_19_2dbba46b-1.x86_64.rpm
hip-hcc3.3.0-3.3.20126.4629_rocm_rel_3.3_19_2dbba46b-1.x86_64.rpm
hip-samples3.3.0-3.3.20126.4629_rocm_rel_3.3_19_2dbba46b-1.x86_64.rpm
hipblas3.3.0-0.24.0.330_rocm_rel_3.3_19_ef9f60d-1.x86_64.rpm
hipcub3.3.0-2.10.0.108_rocm_rel_3.3_19_61fca3e-1.x86_64.rpm
hipsparse3.3.0-1.5.4.237_rocm_rel_3.3_19_961de7b-1.x86_64.rpm
hsa-amd-aqlprofile3.3.0-1.0.0-1.x86_64.rpm
hsa-ext-rocr-dev3.3.0-1.1.30300.0_rocm_rel_3.3_19_23fc088b-1.x86_64.rpm
hsa-rocr-dev3.3.0-1.1.30300.0_rocm_rel_3.3_19_23fc088b-1.x86_64.rpm
hsakmt-roct-devel3.3.0-1.0.9_330_gd84bc09-1.x86_64.rpm
hsakmt-roct3.3.0-1.0.9_330_gd84bc09-1.x86_64.rpm
llvm-amdgpu3.3.0-11.0.dev-1.x86_64.rpm
miopengemm3.3.0-1.1.6.647_rocm_rel_3.3_19_b51a125-1.x86_64.rpm
rccl3.3.0-2.10.0_311_g1d2aa4e_rocm_rel_3.3_19-1.x86_64.rpm
rocalution3.3.0-1.8.1.481_rocm_rel_3.3_19_3e9ad81-1.x86_64.rpm
rocblas3.3.0-2.18.0.2030_rocm_rel_3.3_19_50d99ed0-1.x86_64.rpm
rocfft3.3.0-1.0.1.804_rocm_rel_3.3_19_e732369-1.x86_64.rpm
rocm-bandwidth-test3.3.0-1.4.0.13_rocm_rel_3.3_19_gf671f73-1.x86_64.rpm
rocm-clang-ocl3.3.0-0.5.0.48_rocm_rel_3.3_19_fa039e7-1.x86_64.rpm
rocm-cmake3.3.0-0.3.0.141_rocm_rel_3.3_19_1b9e698-1.x86_64.rpm
rocm-debug-agent3.3.0-1.0.0-1.x86_64.rpm
rocm-dev3.3.0-3.3.0_19-1.x86_64.rpm
rocm-device-libs3.3.0-1.0.0.565_rocm_rel_3.3_19_58abd89-1.x86_64.rpm
rocm-libs3.3.0-3.3.0_19-1.x86_64.rpm
rocm-opencl-devel3.3.0-2.0.0-rocm_rel_3.3_19_363509c8d.x86_64.rpm
rocm-opencl3.3.0-2.0.0-rocm_rel_3.3_19_363509c8d.x86_64.rpm
rocm-smi-lib643.3.0-2.2.0.3.rocm_rel_3.3_19_a482394-1.x86_64.rpm
rocm-smi3.3.0-1.0.0_199_rocm_rel_3.3_19_ga9d6426-1.x86_64.rpm
rocm-utils3.3.0-3.3.0_19-1.x86_64.rpm
rocm-validation-suite3.3.0-3.2.30300-1.x86_64.rpm
rocminfo3.3.0-1.30300.0-1.x86_64.rpm
rocprim3.3.0-2.10.0.974_rocm_rel_3.3_19_6042e8a-1.x86_64.rpm
rocprofiler-dev3.3.0-1.0.0-1.x86_64.rpm
rocrand3.3.0-2.10.0.663_rocm_rel_3.3_19_6f0dadf-1.x86_64.rpm
rocsolver3.3.0-2.7.0.77_rocm_rel_3.3_19_4989200-1.x86_64.rpm
rocsparse3.3.0-1.8.9.764_rocm_rel_3.3_19_593d877-1.x86_64.rpm
rocthrust3.3.0-2.9.0.453_rocm_rel_3.3_19_3de52fa-1.x86_64.rpm
roctracer-dev3.3.0-1.0.0-1.x86_64.rpm
```
# rocminstall.py Example Output on Ubuntu 18.04 system
## To List ROCm 3.3 packages available for installation (will skip rock-dkms if one already installed)
**$ ./rocminstall.py --list --rev 3.3**
```
./rocminstall.py --list --rev 3.3
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  rock-dkms      3.3-19       all          rock-dkms driver in DKMS format.

 Skipping rock-dkms: a version is already installed.
 To install rock-dkms package, please remove installed rock-dkms first. Reboot may be required. 
List of packages selected:



pool/main/M/MIGraphX3.3.0/MIGraphX3.3.0_0.6.0.3793-rocm-rel-3.3-19-d1e945d_amd64.deb
pool/main/M/MIOpen-HIP3.3.0/MIOpen-HIP3.3.0_2.3.0.7730-rocm-rel-3.3-19-ef17912_amd64.deb
pool/main/a/aomp-amdgpu-tests3.3.0/aomp-amdgpu-tests3.3.0_0.7-6_amd64.deb
pool/main/a/aomp-amdgpu3.3.0/aomp-amdgpu3.3.0_0.7-6_amd64.deb
pool/main/a/atmi3.3.0/atmi3.3.0_0.7.11_amd64.deb
pool/main/c/comgr3.3.0/comgr3.3.0_1.6.0.124-rocm-rel-3.3-19-7ac2e34_amd64.deb
pool/main/h/half3.3.0/half3.3.0_1.12.0_amd64.deb
pool/main/h/hcc3.3.0/hcc3.3.0_3.1.20114_amd64.deb
pool/main/h/hip-base3.3.0/hip-base3.3.0_3.3.20126.4629-rocm-rel-3.3-19-2dbba46b_amd64.deb
pool/main/h/hip-doc3.3.0/hip-doc3.3.0_3.3.20126.4629-rocm-rel-3.3-19-2dbba46b_amd64.deb
pool/main/h/hip-hcc3.3.0/hip-hcc3.3.0_3.3.20126.4629-rocm-rel-3.3-19-2dbba46b_amd64.deb
pool/main/h/hip-samples3.3.0/hip-samples3.3.0_3.3.20126.4629-rocm-rel-3.3-19-2dbba46b_amd64.deb
pool/main/h/hipblas3.3.0/hipblas3.3.0_0.24.0.330-rocm-rel-3.3-19-ef9f60d_amd64.deb
pool/main/h/hipcub3.3.0/hipcub3.3.0_2.10.0.108-rocm-rel-3.3-19-61fca3e_amd64.deb
pool/main/h/hipsparse3.3.0/hipsparse3.3.0_1.5.4.237-rocm-rel-3.3-19-961de7b_amd64.deb
pool/main/h/hsa-amd-aqlprofile3.3.0/hsa-amd-aqlprofile3.3.0_1.0.0_amd64.deb
pool/main/h/hsa-ext-rocr-dev3.3.0/hsa-ext-rocr-dev3.3.0_1.1.30300.0-rocm-rel-3.3-19-23fc088b_amd64.deb
pool/main/h/hsa-rocr-dev3.3.0/hsa-rocr-dev3.3.0_1.1.30300.0-rocm-rel-3.3-19-23fc088b_amd64.deb
pool/main/h/hsakmt-roct-dev3.3.0/hsakmt-roct-dev3.3.0_1.0.9-330-gd84bc09_amd64.deb
pool/main/h/hsakmt-roct3.3.0/hsakmt-roct3.3.0_1.0.9-330-gd84bc09_amd64.deb
pool/main/l/llvm-amdgpu3.3.0/llvm-amdgpu3.3.0_11.0.dev_amd64.deb
pool/main/m/miopengemm3.3.0/miopengemm3.3.0_1.1.6.647-rocm-rel-3.3-19-b51a125_amd64.deb
pool/main/m/mivisionx3.3.0/mivisionx3.3.0_1.6.0_amd64.deb
pool/main/r/rccl3.3.0/rccl3.3.0_2.10.0-311-g1d2aa4e-rocm-rel-3.3-19_amd64.deb
pool/main/r/rocalution3.3.0/rocalution3.3.0_1.8.1.481-rocm-rel-3.3-19-3e9ad81_amd64.deb
pool/main/r/rocblas3.3.0/rocblas3.3.0_2.18.0.2030-rocm-rel-3.3-19-50d99ed_amd64.deb
pool/main/r/rocfft3.3.0/rocfft3.3.0_1.0.1.804-rocm-rel-3.3-19-e732369_amd64.deb
pool/main/r/rocm-bandwidth-test3.3.0/rocm-bandwidth-test3.3.0_1.4.0.13-rocm-rel-3.3-19-gf671f73_amd64.deb
pool/main/r/rocm-clang-ocl3.3.0/rocm-clang-ocl3.3.0_0.5.0.48-rocm-rel-3.3-19-fa039e7_amd64.deb
pool/main/r/rocm-cmake3.3.0/rocm-cmake3.3.0_0.3.0.141-rocm-rel-3.3-19-1b9e698_amd64.deb
pool/main/r/rocm-debug-agent3.3.0/rocm-debug-agent3.3.0_1.0.0_amd64.deb
pool/main/r/rocm-dev3.3.0/rocm-dev3.3.0_3.3.0-19_amd64.deb
pool/main/r/rocm-device-libs3.3.0/rocm-device-libs3.3.0_1.0.0.565-rocm-rel-3.3-19-58abd89_amd64.deb
pool/main/r/rocm-libs3.3.0/rocm-libs3.3.0_3.3.0-19_amd64.deb
pool/main/r/rocm-opencl-dev3.3.0/rocm-opencl-dev3.3.0_2.0.0-rocm-rel-3.3-19-363509c8d_amd64.deb
pool/main/r/rocm-opencl3.3.0/rocm-opencl3.3.0_2.0.0-rocm-rel-3.3-19-363509c8d_amd64.deb
pool/main/r/rocm-smi-lib643.3.0/rocm-smi-lib643.3.0_2.2.0.3.rocm-rel-3.3-19-a482394_amd64.deb
pool/main/r/rocm-smi3.3.0/rocm-smi3.3.0_1.0.0-199-rocm-rel-3.3-19-ga9d6426_amd64.deb
pool/main/r/rocm-utils3.3.0/rocm-utils3.3.0_3.3.0-19_amd64.deb
pool/main/r/rocm-validation-suite3.3.0/rocm-validation-suite3.3.0_3.2.30300_amd64.deb
pool/main/r/rocminfo3.3.0/rocminfo3.3.0_1.30300.0_amd64.deb
pool/main/r/rocprim3.3.0/rocprim3.3.0_2.10.0.974-rocm-rel-3.3-19-6042e8a_amd64.deb
pool/main/r/rocprofiler-dev3.3.0/rocprofiler-dev3.3.0_1.0.0_amd64.deb
pool/main/r/rocrand3.3.0/rocrand3.3.0_2.10.0.663-rocm-rel-3.3-19-6f0dadf_amd64.deb
pool/main/r/rocsolver3.3.0/rocsolver3.3.0_2.7.0.77-rocm-rel-3.3-19-4989200_amd64.deb
pool/main/r/rocsparse3.3.0/rocsparse3.3.0_1.8.9.764-rocm-rel-3.3-19-593d877_amd64.deb
pool/main/r/rocthrust3.3.0/rocthrust3.3.0_2.9.0.453-rocm-rel-3.3-19-3de52fa_amd64.deb
pool/main/r/roctracer-dev3.3.0/roctracer-dev3.3.0_1.0.0_amd64.deb
```
