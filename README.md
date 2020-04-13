# rocminstaller
V1.1  
Utility to install ROCm releases directly from ROCm repo  
  
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

