# rocminstaller V1.1 Utility to install ROCm releases directly from ROCm repo  

# $ sudo ./rocminstall.py -h
```
usage: rocminstall.py [-h] [--rev REVSTRING] [--destdir DESTDIR] [--list]  
  
rocminstall.py: utility to download and install ROCm RPMs for specified  
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

```

# Example Output on CentOS system
## To List ROCm 3.3 packages available for installation (will skip rock-dkms if one already installed)
**$ ./rocminstall.py --list --rev 3.3**
```
b'rock-dkms-3.3-19.el7.noarch\n'
 Skipping rock-dkms: a version is already installed.
 To install rock-dkms package, please remove installed rock-dkms first. Reboot may be required. 
List of packages seleted:
MIGraphX-0.6.0.3793-rocm-rel-3.3-19-d1e945da-el7.x86_64.rpm
MIOpen-HIP-2.3.0.7730-rocm-rel-3.3-19-ef17912f-el7.x86_64.rpm
aomp-amdgpu-0.7-6.x86_64.rpm
aomp-amdgpu-tests-0.7-6.x86_64.rpm
atmi-0.7.11-Linux.rpm
comgr-1.6.0.124-rocm-rel-3.3-19-7ac2e34-Linux.rpm
half-1.12.0-el7.x86_64.rpm
hcc-3.1.20114-Linux.rpm
hip-base-3.3.20126.4629-rocm-rel-3.3-19-2dbba46b.x86_64.rpm
hip-doc-3.3.20126.4629-rocm-rel-3.3-19-2dbba46b.x86_64.rpm
hip-hcc-3.3.20126.4629-rocm-rel-3.3-19-2dbba46b.x86_64.rpm
hip-nvcc-3.3.20126.4629-rocm-rel-3.3-19-2dbba46b.x86_64.rpm
hip-samples-3.3.20126.4629-rocm-rel-3.3-19-2dbba46b.x86_64.rpm
hipblas-0.24.0.330-rocm-rel-3.3-19-ef9f60d-el7.x86_64.rpm
hipcub-2.10.0.108-rocm-rel-3.3-19-61fca3e-el7.x86_64.rpm
hipsparse-1.5.4.237-rocm-rel-3.3-19-961de7b-el7.x86_64.rpm
hsa-amd-aqlprofile-1.0.0-Linux.rpm
hsa-ext-rocr-dev-1.1.30300.0-rocm-rel-3.3-19-23fc088b-Linux.rpm
hsa-rocr-dev-1.1.30300.0-rocm-rel-3.3-19-23fc088b-Linux.rpm
hsakmt-roct-1.0.9-330-gd84bc09.x86_64.rpm
hsakmt-roct-devel-1.0.9-330-gd84bc09.x86_64.rpm
kfdtest.rpm
llvm-amdgpu-11.0.dev-1.x86_64.rpm
miopengemm-1.1.6.647-rocm-rel-3.3-19-b51a125-el7.x86_64.rpm
mivisionx-1.6.0-1.x86_64.rpm
rccl-2.10.0-311-g1d2aa4e-rocm-rel-3.3-19-el7.x86_64.rpm
rocalution-1.8.1.481-rocm-rel-3.3-19-3e9ad81-el7.x86_64.rpm
rocblas-2.18.0.2030-rocm-rel-3.3-19-50d99ed0-el7.x86_64.rpm
rocfft-1.0.1.804-rocm-rel-3.3-19-e732369-el7.x86_64.rpm
rocm-bandwidth-test-1.4.0.13-rocm-rel-3.3-19-gf671f73-Linux.rpm
rocm-clang-ocl-0.5.0.48-rocm-rel-3.3-19-fa039e7-el7.x86_64.rpm
rocm-cmake-0.3.0.141-rocm-rel-3.3-19-1b9e698-el7.x86_64.rpm
rocm-debug-agent-1.0.0-Linux.rpm
rocm-dev-3.3.0-19-Linux.rpm
rocm-device-libs-1.0.0.565-rocm-rel-3.3-19-58abd89-Linux.rpm
rocm-dkms-3.3.0-19-Linux.rpm
rocm-libs-3.3.0-19-Linux.rpm
rocm-opencl-2.0.0-rocm-rel-3.3-19-363509c8d-Linux.rpm
rocm-opencl-devel-2.0.0-rocm-rel-3.3-19-363509c8d-Linux.rpm
rocm-smi-1.0.0_199_rocm_rel_3.3_19_ga9d6426-1.x86_64.rpm
rocm-smi-lib64-2.2.0.3.rocm-rel-3.3-19-a482394.rpm
rocm-utils-3.3.0-19-Linux.rpm
rocm-validation-suite-3.2.30300.rpm
rocminfo-1.0.0.0.rocm-rel-3.3-19-70ebe13.rpm
rocprim-2.10.0.974-rocm-rel-3.3-19-6042e8a-el7.x86_64.rpm
rocprofiler-dev-1.0.0-Linux.rpm
rocrand-2.10.0.663-rocm-rel-3.3-19-6f0dadf-Linux.rpm
rocsolver-2.7.0.77-rocm-rel-3.3-19-4989200-el7.x86_64.rpm
rocsparse-1.8.9.764-rocm-rel-3.3-19-593d877-el7.x86_64.rpm
rocthrust-2.9.0.453-rocm-rel-3.3-19-3de52fa-el7.x86_64.rpm
roctracer-dev-1.0.0-Linux.rpm
```

