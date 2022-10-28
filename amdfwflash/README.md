***
# Steps to update IFWI on certain MI200 GPUs using amdfwflash IFWI Updator Tool
***
### TL;DR
1. Blacklist `amdgpu` driver
2. Reboot system
3. Download and execute `amdfwflashinst.py` script
```
wget -O amdfwflashinst.py --no-check-certificate https://raw.githubusercontent.com/srinivamd/rocminstaller/master/amdfwflashinst.py
```
  * List Devices
  ```
  sudo python3 ./amdfwflashinst.py --rev 1.0 --list
  ```
  * Update MI200 IFWI to Maintenance Update #1
  ```
  sudo python3 ./amdfwflashinst.py --rev 1.0 --update
  ```
  * Rollback MI200 IFWI to GA version
  ```
  sudo python3 ./amdfwflashinst.py --rev 1.0 --rollback
  ```
4. Remove `amdgpu` blacklist
5. Reboot the system and verify IFWI version
```
/opt/rocm/bin/rocm-smi --showhw
```
