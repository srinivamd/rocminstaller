#!/usr/bin/env python3
#
# Copyright (c) 2023 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
# Modified by: Sanjay Tripathi (sanjay.tripathi@amd.com)
#
# Download and install the AMDGPU DKMS for the specified ROCm version
# V1.37: 5.5 RC
# V1.36: 5.4.3 GA
# V1.35: 5.4.3 RC
# V1.34: 5.4.2 GA
# V1.33: 5.4.2 RC
# V1.32: 5.4.1 GA
# V1.31: 5.4.1 RC
# V1.30: 5.4 GA
# V1.29: 5.3.3 GA
# V1.28: Ubuntu fix amdgpu-dkms pkgs
# V1.27: 5.3.2 GA
# V1.26: 5.4 RC
# V1.25: Rocky Linux
# V1.24: 5.3 GA, RHEL9 add, drop bionic, centos8
# V1.23: 5.3 RC
# V1.22: add rhel9 for 5.2.3 GA
# V1.21: 5.2.3 GA
# V1.20: 5.2.3 RC
# V1.19: 5.2.2 RC
# V1.18: 5.2.1 GA
# V1.17: 5.2.1 RC
# V1.16: 5.2 GA
# V1.15: fix path to rocm.gpg.key
# V1.14: include libdrm2 amdgpu-core
# V1.13: ROCm 5.2 support
# V1.12: Install libdrm-amdgpu packages
# V1.11: ROCm 5.1.x versions
# V1.10: ROCm 5.1.1 GA
# V1.9: ROCm 5.1 GA
# V1.8: ROCm 5.1 (pre)
# V1.7: ROCm 5.0.2 GA
# V1.6: ROCm 5.0.1 GA
# V1.5: ROCm 5.0 GA
# V1.4: Add support for 5.0.0
# V1.3: Add support for 4.5.1 and 4.5.2
# V1.2: Fix bug in ubuntu install, name change
# V1.0: Initial version 11/2/2021
#
from urllib import request
from urllib.request import urlretrieve
import re
import subprocess
import sys
import argparse
import os
import shlex
import datetime

# Set ROCm Release Package Distribution repo baseURL below
kernurl = { "4.5" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.40/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.40/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.40/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.40/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.40/rhel/7.9/main/x86_64/"
        },
        "4.5.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.40.1/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.40.1/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.40.1/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.40.1/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.40.1/rhel/7.9/main/x86_64/"
        },
        "4.5.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.40.2/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.40.2/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.40.2/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.40.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.40.2/rhel/7.9/main/x86_64/"
        },
        "5.0.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.50/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.50/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.50/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.50/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.50/rhel/7.9/main/x86_64/"
        },
        "5.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.50/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.50/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.50/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.50/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.50/rhel/7.9/main/x86_64/"
        },
        "5.0.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.50.1/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.50.1/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.50.1/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.50.1/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.50.1/rhel/7.9/main/x86_64/"
        },
        "5.0.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/21.50.2/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/21.50.2/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/21.50.2/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/21.50.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/21.50.2/rhel/7.9/main/x86_64/"
        },
        "5.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.10/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.10/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.10/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.10/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.10/rhel/7.9/main/x86_64/"
        },
        "5.1.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.10/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.10/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.10/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.10/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.10/rhel/7.9/main/x86_64/"
        },
        "5.1.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.10.1/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.10.1/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.10.1/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.10.1/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.10.1/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.10.1/rhel/7.9/main/x86_64/"
        },
        "5.1.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.10.2/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.10.2/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.10.2/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.10.2/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.10.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.10.2/rhel/7.9/main/x86_64/"
        },
        "5.1.3" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.10.3/sle/15/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.10.3/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.10.3/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.10.3/rhel/8.4/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.10.3/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.10.3/rhel/7.9/main/x86_64/"
        },
        "5.2.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.20/sle/15.3/main/x86_64/",
        "sles154" : "https://repo.radeon.com/amdgpu/22.20/sle/15.4/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.4/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/22.20/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.20/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.20/rhel/7.9/main/x86_64/"
        },
        "5.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.20/sle/15.3/main/x86_64/",
        "sles154" : "https://repo.radeon.com/amdgpu/22.20/sle/15.4/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.20/rhel/8.4/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/22.20/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.20/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.20/rhel/7.9/main/x86_64/"
        },
        "5.2.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.20.1/sle/15.3/main/x86_64/",
        "sles154" : "https://repo.radeon.com/amdgpu/22.20.1/sle/15.4/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.20.1/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.20.1/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.20.1/rhel/8.4/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/22.20.1/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.20.1/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.20.1/rhel/7.9/main/x86_64/"
        },
        "5.2.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/.22.20.2/sle/15.3/main/x86_64/",
        "sles154" : "https://repo.radeon.com/amdgpu/.22.20.2/sle/15.4/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/.22.20.2/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/.22.20.2/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/.22.20.2/rhel/8.4/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/.22.20.2/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/.22.20.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/.22.20.2/rhel/7.9/main/x86_64/"
        },
        "5.2.3" :
        { "sles" : "https://repo.radeon.com/amdgpu/22.20.3/sle/15.3/main/x86_64/",
        "sles154" : "https://repo.radeon.com/amdgpu/22.20.3/sle/15.4/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/8.6/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/8.5/main/x86_64/",
        "centos84" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/8.4/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/9.0/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/22.20.3/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/22.20.3/rhel/7.9/main/x86_64/"
        },
        "5.3.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.3/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.3/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.3/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.3/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.3/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.3/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.3/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.3/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.3/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.3/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.3/rhel/7.9/main/x86_64/"
        },
        "5.3.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.3.2/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.3.2/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.3.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.3.2/rhel/7.9/main/x86_64/"
        },
        "5.3.3" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.3.3/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.3.3/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.3.3/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.3.3/rhel/7.9/main/x86_64/"
        },
        "5.4.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.4/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.4/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.4/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.4/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.4/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.4/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.4/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.4/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.4/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.4/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.4/rhel/7.9/main/x86_64/"
        },
        "5.4.1" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.4.1/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.4.1/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.4.1/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.4.1/rhel/7.9/main/x86_64/"
        },
        "5.4.2" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.4.2/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.4.2/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.4.2/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.4.2/rhel/7.9/main/x86_64/"
        },
        "5.4.3" :
        { "sles" : "https://repo.radeon.com/amdgpu/5.4.3/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/5.4.3/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/5.4.3/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/5.4.3/rhel/7.9/main/x86_64/"
        },
        "5.5.0" :
        { "sles" : "https://repo.radeon.com/amdgpu/.5.5/sle/15.4/main/x86_64/",
        "sles153" : "https://repo.radeon.com/amdgpu/.5.5/sle/15.3/main/x86_64/",
        "centos8" : "https://repo.radeon.com/amdgpu/.5.5/rhel/8.7/main/x86_64/",
        "rhel8" : "https://repo.radeon.com/amdgpu/.5.5/rhel/8.7/main/x86_64/",
        "centos85" : "https://repo.radeon.com/amdgpu/.5.5/rhel/8.5/main/x86_64/",
        "centos86" : "https://repo.radeon.com/amdgpu/.5.5/rhel/8.6/main/x86_64/",
        "centos9" : "https://repo.radeon.com/amdgpu/.5.5/rhel/9.1/main/x86_64/",
        "rhel9" : "https://repo.radeon.com/amdgpu/.5.5/rhel/9.1/main/x86_64/",
        "rhel90" : "https://repo.radeon.com/amdgpu/.5.5/rhel/9.0/main/x86_64/",
        "ubuntu" : "https://repo.radeon.com/amdgpu/.5.5/ubuntu",
        "centos" : "https://repo.radeon.com/amdgpu/.5.5/rhel/7.9/main/x86_64/"
        }
    }

# Commands
RM_F_CMD = "/bin/rm -f "
RPM_CMD = "/usr/bin/rpm"
YUM_CMD = "/usr/bin/yum"
DPKG_CMD = "/usr/bin/dpkg"
DPKGDEB_CMD = "/usr/bin/dpkg-deb"
APTGET_CMD = "/usr/bin/apt-get"
APT_CMD = "/usr/bin/apt"
APTKEY_CMD = "/usr/bin/apt-key"
WGET_CMD = "/usr/bin/wget"
ZYPPER_CMD = "/usr/bin/zypper"
ECHO_CMD = "/bin/echo"
TEE_CMD = "/usr/bin/tee"

# Package type suffixes
PKGTYPE_RPM = "rpm"
PKGTYPE_DEB = "deb"

# Supported OS types
CENTOS_TYPE = "centos" # Version 7
CENTOS8_TYPE = "centos8"
CENTOS9_TYPE = "centos9"
UBUNTU_TYPE = "ubuntu"
DEBIAN_TYPE = "debian"
SLES_TYPE = "sles"
RHEL_TYPE = "rhel" # Version 7
RHEL8_TYPE = "rhel8"
RHEL9_TYPE = "rhel9"
ROCKY_LINUX_TYPE = "Rocky Linux"

CENTOS_VERSION8_TYPESTRING = 'VERSION="8'
CENTOS_VERSION9_TYPESTRING = 'VERSION="9'
RHEL_VERSION8_TYPESTRING = 'VERSION="8'
RHEL_VERSION9_TYPESTRING = 'VERSION="9'

BIONIC_TYPE = "bionic"
FOCAL_TYPE = "focal"
JAMMY_TYPE = "jammy"


# OS release info
ETC_OS_RELEASE = "/etc/os-release"
# Download destination dir: default current director
DOWNLOAD_DESTDIR = "./"

#
# Is rock-dkms already installed? True if already installed
#
def check_rock_dkms(pkgtype):
    check_cmd = {
        PKGTYPE_RPM : RPM_CMD + " -q rock-dkms ",
        PKGTYPE_DEB : DPKG_CMD + " -l rock-dkms ",
    }[pkgtype]
    if pkgtype is PKGTYPE_RPM:
        check_cmd = RPM_CMD + " -q rock-dkms"
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            return True
        except subprocess.CalledProcessError as err:
            #return False
            pass

        # check for amdgpu-dkms
        check_cmd = RPM_CMD + " -q amdgpu-dkms"
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            return True
        except subprocess.CalledProcessError as err:
            return False
    elif pkgtype is PKGTYPE_DEB:
        check_cmd = DPKG_CMD + " -l rock-dkms"
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            for line in str.splitlines(ps1.stdout.decode('utf-8')):
                if re.search(r'^i.*rock-dkms.*all', line): # 'i' for installed
                    return True
        except subprocess.CalledProcessError as err:
            pass

        check_cmd = DPKG_CMD + " -l amdgpu-dkms"
        try:
            ps1 = subprocess.run(check_cmd.split(), stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, check=True)
            print(ps1.stdout.decode('utf-8'))
            for line in str.splitlines(ps1.stdout.decode('utf-8')):
                if re.search(r'^i.*amdgpu-dkms.*all', line): # 'i' for installed
                    return True
            return False
        except subprocess.CalledProcessError as err:
            return False
    else:
        print("Unknown package type {}. Cannot detect rock-dkms amdgpu-dkms status.".format(pkgtype))
        return False

# Get the list of ROCm rpm packages from the ROCm release URL
rockset = set()
rocklist = []
# debian/ubuntu
#
# select amdgpu-dkms and amdgpu-dkms-firmware packages
#
# debian/ubuntu
def get_deb_pkglist(rocmurl, pkgtype, ubuntutype):
    global rocklist
    urlpath = rocmurl + "/dists/" + ubuntutype + "/main/binary-amd64/Packages"
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'Filename: pool.*\.{pkgtype}', line)
            if mat:
                pkgname = line[mat.start()+len("Filename: "):mat.end()]
                if ("amdgpu-dkms".lower() in pkgname.lower()
                    or "amdgpu-core".lower() in pkgname.lower()
                    or "libdrm2-amdgpu".lower() in pkgname.lower()
                    or "libdrm-amdgpu".lower() in pkgname.lower()):
                        rockset.add(pkgname)
                        continue
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" NOTE: amdgpu-dkms: a version is already installed.")
            print((" To install amdgpu-dkms package, please remove installed amdgpu-dkms"
                   " first, reboot, and then install amdgpu-dkms packages. "))
            rocklist = None
        else:
            rocklist = list(rockset)
    except Exception as e:
        rocklist = None
        print(urlpath + " : " + str(e))

def get_pkglist(rocmurl, pkgtype):
    global rocklist
    urlpath = rocmurl
    try:
        urld = request.urlopen(urlpath)
        for line in str.splitlines(urld.read().decode('utf-8'), True):
            mat = re.search(rf'".*\.{pkgtype}"', line)
            if mat:
                pkgname = line[mat.start()+1:mat.end()-1]
                if ("amdgpu-dkms".lower() in pkgname.lower()
                    or "amdgpu-core".lower() in pkgname.lower()
                    or "libdrm2-amdgpu".lower() in pkgname.lower()
                    or "libdrm-amdgpu".lower() in pkgname.lower()):
                        rockset.add(pkgname)
                        continue
        # return set as a list
        if check_rock_dkms(pkgtype) is True:
            # remove rock-dkms and rock-dkms-firmware from list
            print(" NOTE: amdgpu-dkms: a version is already installed.")
            print((" To install amdgpu-dkms package, please remove installed amdgpu-dkms"
                   " first, reboot, and then install amdgpu-dkms packages. "))
            rocklist = None
        else:
            rocklist = list(rockset)
    except Exception as e:
        rocklist = None
        print(urlpath + " : " + str(e))

# Download and install packages utility functions
def download_and_install_deb(args, rocmbaseurl, pkgname):
    global rocklist
    if args.repourl:
        fetchurl = args.repourl[0] + "/"
    else:
        if args.baseurl is None:
            fetchurl = rocmbaseurl + "/"
        else:
            fetchurl = rocmbaseurl + "/"
    rmcmd = RM_F_CMD
    aptinstcmd = APT_CMD + " install -y "
    aptgetcmd = APTGET_CMD + " -y -f install "
    # download destdir
    urlretrieve(fetchurl + pkgname, args.destdir[0] + "/" + os.path.basename(pkgname))
    execcmd = aptinstcmd + args.destdir[0] + "/" + os.path.basename(pkgname) + " "
    rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(pkgname) + " "
    try:
        ps1 = subprocess.Popen(execcmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
    try:
        ps1 = subprocess.Popen(aptgetcmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
    try:
        ps2 = subprocess.Popen(rmcmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")

def setup_sles_zypp_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # Set up rocm repo for chosen rev to install
        # use rev specific rocm repo
        zypprepo = "[amdgpu" + args.revstring[0] + "]\nenabled=1\nautorefresh=0\nbaseurl=" + fetchurl + "\ntype=rpm-md\ngpgcheck=0"
        echocmd = ECHO_CMD + " -e '" + zypprepo + "' "
        repofilename = "/etc/zypp/repos.d/amdgpu" + args.revstring[0] + ".repo "
        teecmd = TEE_CMD + " " + repofilename + " "
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # apt update repo
        zypprefresh = ZYPPER_CMD + " refresh "
        try:
            ps1 = subprocess.Popen(zypprefresh.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_centos_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # Set up rocm repo for chosen rev to install
        # use rev specific rocm repo
        yumrepo = "[AMDGPU" + args.revstring[0] +"]\nname=AMDGPU\nbaseurl=" + fetchurl + "\nenabled=1\ngpgcheck=0"
        echocmd = ECHO_CMD + " -e '" + yumrepo + "' "
        repofilename = "/etc/yum.repos.d/amdgpu" + args.revstring[0] + ".repo"
        teecmd = TEE_CMD + " " + repofilename + " "
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # clean repo
        yumupdate = YUM_CMD + " clean all "
        try:
            ps1 = subprocess.Popen(yumupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_centos9_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        setup_centos_repo(args, fetchurl)

def setup_centos8_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        setup_centos_repo(args, fetchurl)

def remove_centos_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/yum.repos.d/amdgpu" + args.revstring[0] + ".repo"
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        yumupdate = YUM_CMD + " clean all "
        try:
            ps1 = subprocess.Popen(yumupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def remove_sles_zypp_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/zypp/repos.d/amdgpu" + args.revstring[0] + ".repo "
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        zyppclean = ZYPPER_CMD + " clean "
        try:
            ps1 = subprocess.Popen(zyppclean.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

def setup_debian_repo(args, fetchurl, ubuntutype):
    global rocklist

    if args.repourl:
        pass
    else:
        # Set up rocm repo for chosen rev to install
        wgetkey = WGET_CMD + " -q -O - http://repo.radeon.com/rocm/rocm.gpg.key "
        aptkeycmd = APTKEY_CMD + " add -"
        try:
            ps1 = subprocess.Popen(wgetkey.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(aptkeycmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # use rev specific rocm repo
        debrepo = "deb [arch=amd64] " + fetchurl + " " + ubuntutype + " main "
        echocmd = ECHO_CMD + " '" + debrepo + "' "
        repofilename = "/etc/apt/sources.list.d/amdgpu" + args.revstring[0] + ".list "
        teecmd = TEE_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(shlex.split(echocmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ps2 = subprocess.Popen(teecmd.split(), stdin=ps1.stdout, stdout=subprocess.PIPE)
            ps1.stdout.close()
            out = ps2.communicate()[0]
            print(out.decode('utf-8'))
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # apt update repo
        aptupdate = APT_CMD + " clean"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        # apt update repo
        aptupdate = APT_CMD + " update"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)

        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)



def remove_debian_repo(args, fetchurl):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        # remove rocm repo for chosen rev to install
        # use rev specific rocm repo
        repofilename = "/etc/apt/sources.list.d/amdgpu" + args.revstring[0] + ".list "
        rmrepocmd = RM_F_CMD + " " + repofilename
        try:
            ps1 = subprocess.Popen(rmrepocmd.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)
        # clean repo
        # apt update repo
        aptupdate = APT_CMD + " clean"
        try:
            ps1 = subprocess.Popen(aptupdate.split(), bufsize=0).communicate()[0]
        except subprocess.CalledProcessError as err:
            for line in str.splitlines(err.output.decode('utf-8')):
                print(line)


# On Ubuntu, use the steps below to install downloaded deb
def download_install_rocm_deb(args, rocmbaseurl, ubuntutype):
    global rocklist

    if args.repourl:
        pass
        # use rev specific rocm repo
    else:
        if args.baseurl is None:
            fetchurl = rocmbaseurl + "/"
        else:
            fetchurl = rocmbaseurl + "/"
        # Set up rocm repo for chosen rev to install
        setup_debian_repo(args, fetchurl, ubuntutype)

    # Download and install from custom repo URL
    rmcmd = RM_F_CMD
    aptinstcmd = APT_CMD + " install -y "
    aptgetcmd = APTGET_CMD + " -y -f install "
    if rocklist:
        # install amdgpu-dkms-firmware first
        pkgn = [ x for x in rocklist if "amdgpu-dkms-firmware" in x ]
        if pkgn:
            # remove amdgpu-dkms-firmware from list
            rocklist = [ x for x in rocklist if "amdgpu-dkms-firmware" not in x ]
            # Download and Install amdgpu-dkms-firmware first (assumes only one)
            download_and_install_deb(args, rocmbaseurl, pkgn[0])
        if rocklist:
            for pkgn in rocklist:
                download_and_install_deb(args, rocmbaseurl, pkgn)

    return


#
# --rev REV is the ROCm version number string
# --destdir DESTDIR directory to download rpm for installation
#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('[V1.37]amdgpuinst.py: utility to '
        ' download and install AMDGPU DKMS ROCm packages for specified rev'
        ' (dkms, kernel headers must be installed, requires sudo privilege) '),
        prefix_chars='-')
    parser.add_argument('--rev', nargs=1, dest='revstring', default='rpm',
        help=('specifies ROCm release version '
              ' Example: --rev 4.5 for ROCm 4.5 or --rev 4.5.1 for ROCm 4.5.1'
              )
              )
    parser.add_argument('--destdir', nargs=1, dest='destdir', default='.',
        help=('specify directory where to download RPM'
              ' before installation. Default: current directory '
              ' --destdir /tmp to use /tmp directory')
              )
    parser.add_argument('--list', dest='listonly', action='store_true',
        help=('just list the packages that will be installed'
              ' -- do not download or install ')
              )
    parser.add_argument('--repourl', nargs=1, dest='repourl', default=None,
        help=('specify ROCm repo URL to use from where to download packages'
              ' as in http://repo.radeon.com/amdgpu/{apt, yum, zyp, centos8}/<REV> '
              ' Example: --repourl http://compute-artifactory/build/xyz')
              )
    parser.add_argument('--baseurl', nargs=1, dest='baseurl', default=None,
        help=('specify early access ROCm repo URL to use from where to download packages'
              ' as in http://repo.radeon.com/amdgpu/{apt, yum, zyp, centos8}/.. '
              ' Example: --baseurl http://repo.radeon.com/amdgpu/private/bionic/')
              )

    args = parser.parse_args();

    # Determine installed OS type
    ostype = None
    with open(ETC_OS_RELEASE, 'r') as f:
        for line in f:
            if ROCKY_LINUX_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
                break
            if CENTOS_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
                break
            if DEBIAN_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                break
            if JAMMY_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = JAMMY_TYPE
                break
            if FOCAL_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = FOCAL_TYPE
                break
            if BIONIC_TYPE.lower() in line.lower():
                ostype = UBUNTU_TYPE
                ubuntutype = BIONIC_TYPE
                break
            if SLES_TYPE.lower() in line.lower():
                ostype = SLES_TYPE
                break
            if RHEL_TYPE.lower() in line.lower():
                ostype = CENTOS_TYPE
                break

    # Detect CentOS8/RHEL8 to set the correct ROCm repo
    if ostype is CENTOS_TYPE:
        with open(ETC_OS_RELEASE, 'r') as f:
            for line in f:
                if CENTOS_VERSION8_TYPESTRING.lower() in line.lower():
                    ostype = CENTOS8_TYPE
                    break
                if RHEL_VERSION8_TYPESTRING.lower() in line.lower():
                    ostype = CENTOS8_TYPE
                    break
                if CENTOS_VERSION9_TYPESTRING.lower() in line.lower():
                    ostype = RHEL9_TYPE
                    break
                if RHEL_VERSION9_TYPESTRING.lower() in line.lower():
                    ostype = RHEL9_TYPE
                    break

    if ostype is None:
        print("Exiting: Unknown installed OS type")
        parser.print_help()
        sys.exit(1)

    # Log version and date of run
    print("Running V1.37 amdgpuinst.py utility for OS: " + ostype + " on: " + str(datetime.datetime.now()))

    #
    # Set pkgtype to use based on ostype
    #
    pkgtype = None
    pkgtype = {
        RHEL9_TYPE : PKGTYPE_RPM,
        RHEL8_TYPE : PKGTYPE_RPM,
        CENTOS8_TYPE : PKGTYPE_RPM,
        CENTOS_TYPE : PKGTYPE_RPM,
        UBUNTU_TYPE : PKGTYPE_DEB,
        SLES_TYPE : PKGTYPE_RPM
    }[ostype]

    #
    # Get the list of package names from repo using --rev option
    #
    if args.repourl:
        rocmbaseurl = args.repourl[0]
    elif args.baseurl:
        rocmbaseurl = args.baseurl[0]
    else:
        if args.revstring[0] in kernurl:
            rocmbaseurl = kernurl[args.revstring[0]][ostype]
        else:
            print("Exiting: No AMDGPU DKMS package for specified rev: ", args.revstring[0])
            sys.exit(1)

    if args.repourl:
        get_pkglist(args.repourl[0] + "/", pkgtype)
    if args.baseurl:
        if pkgtype is PKGTYPE_DEB:
            get_deb_pkglist(rocmbaseurl, pkgtype, ubuntutype)
        else:
            get_pkglist(rocmbaseurl, pkgtype)
    else:
        if pkgtype is PKGTYPE_DEB:
            get_deb_pkglist(rocmbaseurl + "/", pkgtype, ubuntutype)
        else:
            get_pkglist(rocmbaseurl + "/", pkgtype)

    #
    # Based on os type, set the package install command and options
    #
    cmd = {
       RHEL9_TYPE : YUM_CMD + " localinstall --skip-broken --assumeyes ",
       RHEL8_TYPE : YUM_CMD + " localinstall --skip-broken --assumeyes ",
       CENTOS8_TYPE : YUM_CMD + " localinstall --skip-broken --assumeyes ",
       CENTOS_TYPE : YUM_CMD + " localinstall --skip-broken --assumeyes ",
       UBUNTU_TYPE : APTGET_CMD + " --no-download --ignore-missing -y install ",
       SLES_TYPE : ZYPPER_CMD + " --no-gpg-checks install --allow-unsigned-rpm --no-recommends "
    }[ostype]

    #
    # If rocklist is None, print help and exit
    #
    if rocklist is None:
        parser.print_help()
        sys.exit(1)

    #
    # If --list specified, print the package list and exit
    #
    if args.listonly is True:
        print("List of packages selected:\n")
        print('\n'.join(sorted(rocklist)))
        sys.exit(0)

    #
    # Download and install the selected packages
    # Ubuntu/Debian dpkg/apt does not have an easy method to use dpkg, apt
    # to install downloaded deb packages with dependencies equivalent
    # yum localinstall command on CentOS, SLES.
    # So call a debian specific function for Ubuntu/Debian
    #
    # for Ubuntu/Debian
    if ostype is UBUNTU_TYPE:
        download_install_rocm_deb(args, rocmbaseurl, ubuntutype)
        remove_debian_repo(args, rocmbaseurl)
        sys.exit(0)

    # for CentOS and SLES use the following
    execcmd = cmd
    rmcmd = RM_F_CMD
    if args.repourl:
        fetchurl = args.repourl[0] + "/"
    else:
        if args.baseurl is None:
            fetchurl = rocmbaseurl + "/"
        else:
            fetchurl = rocmbaseurl + "/"

    if ostype is CENTOS_TYPE:
        setup_centos_repo(args, fetchurl)
    elif ostype is CENTOS8_TYPE:
        setup_centos8_repo(args, fetchurl)
    elif ostype is RHEL9_TYPE:
        setup_centos9_repo(args, fetchurl)
    else:
        setup_sles_zypp_repo(args, fetchurl)

    for n in sorted(rocklist):
        # download to destdir
        urlretrieve(fetchurl + n, args.destdir[0] + "/" + os.path.basename(n))
        execcmd = execcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        rmcmd = rmcmd + args.destdir[0] + "/" + os.path.basename(n) + " "
        print('.', end='', flush=True)

    try:
        ps1 = subprocess.Popen(execcmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        print(" Unexpected error encountered! Did you forget sudo?")

    try:
        ps2 = subprocess.Popen(rmcmd.split(), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)

    if ostype is CENTOS_TYPE or ostype is CENTOS8_TYPE or ostype is RHEL9_TYPE:
        remove_centos_repo(args, fetchurl)
    else:
        remove_sles_zypp_repo(args, fetchurl)

    sys.exit(0)
