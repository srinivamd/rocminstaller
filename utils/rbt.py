#!/usr/bin/env python3
#
# Copyright (c) 2020 Advanced Micro Devices, Inc. All Rights Reserved.
#
# Author: Srinivasan Subramanian (srinivasan.subramanian@amd.com)
#
# Wrapper to run rocm-bandwidth-test traffic between CPUs and GPUs
#
# V1.5: remove HSA_REV_COPY
# V1.4: Add --ncpu and --ngpu options
# V1.3: Add rev_copy_dir
# V1.2: Trim to 2 decimals
# V1.1: Nicer output
# V1.0: ncpus=2, ngpus=8 hardcoded
#

import os
import subprocess
import sys
import shlex
import argparse

bwout = [ ["" for i in range(10)] for j in range(10) ]

def run_rbt_topo(rbtpath):
    rbt_cmd = rbtpath + " -t "
    try:
        ps1 = subprocess.Popen(shlex.split(rbt_cmd), bufsize=0).communicate()[0]
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)

def run_rbt(rbtpath, src, dst, unidir=False):
    if unidir is True:
        rbt_cmd = rbtpath + " -m 512 -s " + str(src) + " -d " + str(dst)
    else:
        rbt_cmd = rbtpath + " -m 512 -b " + str(src) + "," + str(dst)
    grep_cmd = "/bin/grep MB"
    awk_cmd = "/usr/bin/awk '{print $6}'"
    try:
        ps1 = subprocess.Popen(shlex.split(rbt_cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=os.environ)
        ps2 = subprocess.Popen(shlex.split(grep_cmd), stdin=ps1.stdout, stdout=subprocess.PIPE)
        ps3 = subprocess.Popen(shlex.split(awk_cmd), stdin=ps2.stdout, stdout=subprocess.PIPE)
        ps1.stdout.close()
        ps2.stdout.close()
        out = ps3.communicate()[0]
#        print(out.decode('utf-8').strip())
        return out.decode('utf-8').strip()
    except subprocess.CalledProcessError as err:
        for line in str.splitlines(err.output.decode('utf-8')):
            print(line)
        return " N/A "

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=('[V1.5]rbt.py: Wrapper to '
        ' run rocm-bandwidth-test from ROCm release installation'),
        prefix_chars='-')
    parser.add_argument('--rev', nargs=1, dest='revstring', default=None,
        help=('specifies ROCm release installation to use '
              ' Example: --rev 3.5.0 to use /opt/rocm-3.5.0/bin/rocm-bandwidth-test'
              ' or '
              ' --rev 3.6.0 to use /opt/rocm-3.6.0/bin/rocm-bandwidth-test')
              )
    parser.add_argument('--ncpu', nargs=1, dest='ncpus', type=int, default=2,
        help=('specifies number of CPU devices, default 2 '
              ' --ncpu 4 to specify 4 CPU devices/agents')
              )
    parser.add_argument('--ngpu', nargs=1, dest='ngpus', type=int, default=8,
        help=('specifies number of CPU devices, default 2 '
              ' --ncpu 4 to specify 4 CPU devices/agents')
              )
    args = parser.parse_args();

    if args.revstring:
        rbtloc = "/opt/rocm-" + args.revstring[0] + "/bin/rocm-bandwidth-test"
    else:
        rbtloc = "/opt/rocm-3.6.0/bin/rocm-bandwidth-test"
    ncpus = args.ncpus
    ngpus = args.ngpus
    print("[V1.5]rbt.py Using: {0} NCPU={1} NGPU={2}".format(rbtloc, ncpus, ngpus))
    run_rbt_topo(rbtloc)

    print("Starting unidirectional test.");
    for i in range(ncpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)

    print("\n=== Unidirectional BW: using 512 MB transfers:====")
    print("{0:^10}".format(""),end=' ')
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
    print("")
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
        for j in range(ncpus + ngpus):
            print("{0:10}".format(bwout[i][j][0:5]),end=' ')
        print("")

    print("Starting bidirectional test.");
    for i in range(ncpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)

    print("\n===== Bidirectional BW: using 512 MB transfers:====")
    print("{0:^10}".format(""),end=' ')
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
    print("")
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
        for j in range(ncpus + ngpus):
            print("{0:10}".format(bwout[i][j][0:5]),end=' ')
        print("")

    sys.exit(0)
    print("HSA_REV_COPY_DIR=1 Starting unidirectional test.");
    os.environ['HSA_REV_COPY_DIR'] = '1'
    for i in range(ncpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, True)
            print(j, end='', flush=True)

    print("\n=== HSA_REV_COPY_DIR=1 Unidirectional BW: using 512 MB transfers:====")
    print("{0:^10}".format(""),end=' ')
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
    print("")
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
        for j in range(ncpus + ngpus):
            print("{0:10}".format(bwout[i][j][0:5]),end=' ')
        print("")

    print("HSA_REV_COPY_DIR=1 Starting bidirectional test.");
    for i in range(ncpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)
    for i in range(ncpus,ncpus+ngpus):
        for j in range(ncpus,ncpus+ngpus):
            bwout[i][j] = run_rbt(rbtloc, i, j, False)
            print(j, end='', flush=True)

    print("\n===== HSA_REV_COPY_DIR=1 Bidirectional BW: using 512 MB transfers:====")
    print("{0:^10}".format(""),end=' ')
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
    print("")
    for i in range(ncpus + ngpus):
        print("{0:^10}".format(i),end=' ')
        for j in range(ncpus + ngpus):
            print("{0:10}".format(bwout[i][j][0:5]),end=' ')
        print("")

    sys.exit(0)
