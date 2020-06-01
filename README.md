# rocminstaller V1.6 Utility to install ROCm releases directly from ROCm repo
# rocm_techsupport.sh V1.1 Shell Utility for Ubuntu/CentOS/SLES log collection

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
# $ sudo sh <path_to>/rocm_techsupport.sh 2>&1 | tee <path_to>/rocm_techsupport.logs
```
Example: Run rocm_techsupport.sh in current directory ('.') and save standard output and errors in /tmp/rocm_techsupport.log
# sudo sh ./rocm_techsupport.sh 2>&1 | tee /tmp/rocm_techsupport.log

Compress/Zip the output file and include with reported issue.
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
