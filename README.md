# [Unofficial But Works!] rocm_techsupport.sh V1.10 Shell Utility for Ubuntu/CentOS/SLES/docker log collection from last 3 boots
# NOTE: To enable persistent boot logs across reboots, please run:  
***sudo mkdir -p /var/log/journal***

***sudo systemctl restart systemd-journald.service***

***Example Usage:***

***mkdir  downloads***

***cd  downloads***

***wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocm_techsupport.sh***

***$ sudo sh <path_to>/rocm_techsupport.sh 2>&1 | tee <path_to>/rocm_techsupport.logs***
```
Example: Run rocm_techsupport.sh in current directory ('.') and save standard output and 
errors in /tmp/rocm_techsupport.log

# sudo sh ./rocm_techsupport.sh 2>&1 | tee /tmp/rocm_techsupport.log

Compress/Zip the output file and include with reported issue.
```

# [Unofficial But Works!] rocminstaller V1.11 Utility (requires Python3) to install ROCm releases on Ubuntu/Debian/CentOS7/RHEL7/CentOS8/RHEL8/SLES15 OS
#### NOTE: Install dkms, kernel headers packages on OS BEFORE installing ROCm
#### NOTE: On SLES15, the script uses zypper and requires user interaction
#### Download it using:
***wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py***

```
Example: Install ROCm 3.5, including kernel components (assumes dkms, kernel header
preinstalled)

sudo ./rocminstall.py --rev 3.5

Example: Install ROCm 3.3 development packages (no kernel components)

sudo ./rocminstall.py --rev 3.5 --nokernel

```

```
./rocminstall.py --help
usage: rocminstall.py [-h] [--rev REVSTRING] [--destdir DESTDIR] [--list]
                      [--repourl REPOURL] [--nokernel]

[V1.11]rocminstall.py: utility to download and install ROCm packages for
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
  --nokernel         do not install rock kernel packages, for example, used to
                     install ROCm in docker
```

