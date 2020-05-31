# rocminstaller V1.1 Utility to install ROCm releases directly from ROCm repo  

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

# Example Output on CentOS system
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

