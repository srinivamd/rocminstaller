# rocm_techsupport.sh V1.18 Shell Utility for Ubuntu/CentOS/SLES/docker log collection from last 3 boots
### NOTE: To enable persistent boot logs across reboots, please run:  
***sudo mkdir -p /var/log/journal*** 

***sudo systemctl restart systemd-journald.service*** 

### Download using:
***wget -O --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocm_techsupport.sh*** 

### Example Usage:
```
mkdir  downloads
cd  downloads
wget -O --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocm_techsupport.sh

#Redirect output to file with <SYSTEM_NAME> and date prefixed-name
sudo sh ./rocm_techsupport.sh > <SYSTEM_NAME>.`date +"%y-%m-%d-%H-%M-%S"`.rocm_techsupport.log 2>&1

NOTE: Use of back quotes (`) in above command to get a date timestamp based filename
Compress/Zip the output file and include with reported issue.
```

# [Supports 3.3, 3.5, 3.7, 3.8] V1.17 rocminstall.py Utility to install ROCm releases. Supports Ubuntu/Debian, CentOS/RHEL 7/8, SLES15 installation
#### NOTE: Install dkms, kernel headers, gcc packages on OS BEFORE installing ROCm
#### NOTE: On SLES15, the script uses zypper and requires user interaction
#### Download using:
***wget -O --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py***

```
Example: Install ROCm 3.7, including kernel components (assumes dkms, kernel header, gcc
preinstalled)
wget -O --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/rocminstall.py

sudo python3 ./rocminstall.py --rev 3.7

Example: Install ROCm 3.5 development packages (no kernel components)

sudo python3 ./rocminstall.py --rev 3.5 --nokernel

```
#### Usage
```
usage: rocminstall.py [-h] [--rev REVSTRING] [--destdir DESTDIR] [--list]
                      [--repourl REPOURL] [--baseurl BASEURL] [--nokernel]
                      [--justkernel]

[V1.17]rocminstall.py: utility to download and install ROCm packages for
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
  --baseurl BASEURL  specify early access ROCm repo URL to use from where to
                     download packages Example: --baseurl
                     http://repo.radeon.com/rocm/private/apt_3.6-priv/
  --nokernel         do not install rock kernel packages, for example, used to
                     install ROCm in docker
  --justkernel       ONLY install rock kernel packages of specified version -
                     undefined behavior if --nokernel also specified

```

