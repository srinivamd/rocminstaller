# [Unofficial But Works!] rocm_techsupport.sh V1.14 Shell Utility for Ubuntu/CentOS/SLES/docker log collection from last 3 boots
### NOTE: To enable persistent boot logs across reboots, please run:  
***sudo mkdir -p /var/log/journal*** 

***sudo systemctl restart systemd-journald.service*** 

### Download using:
***wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocm_techsupport.sh*** 

### Example Usage:
```
mkdir  downloads
cd  downloads
wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocm_techsupport.sh

#Redirect output to file with date prefixed-name
sudo sh ./rocm_techsupport.sh > `date +"%y-%m-%d-%H-%M-%S"`.rocm_techsupport.log 2>&1

NOTE: Use of back quotes (`) in above command to get a date timestamp based filename
Compress/Zip the output file and include with reported issue.
```

# [Unofficial But Works!] V1.15 rocminstall.py Utility to install ROCm releases. Supports Ubuntu/Debian, CentOS7/RHEL7, CentOS8/RHEL8, SLES15 installation
#### NOTE: Install dkms, kernel headers packages on OS BEFORE installing ROCm
#### NOTE: On SLES15, the script uses zypper and requires user interaction
#### Download using:
***wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py***

```
Example: Install ROCm 3.5, including kernel components (assumes dkms, kernel header
preinstalled)
wget --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py

sudo ./rocminstall.py --rev 3.5

Example: Install ROCm 3.3 development packages (no kernel components)

sudo ./rocminstall.py --rev 3.3 --nokernel

```
#### Usage
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

