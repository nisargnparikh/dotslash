#!/usr/bin/python3

import subprocess
import time

processes = []
for run in range(3):
    print('Starting Run: ', run)
    print('================================================================\n\n')
    if run == 0:
        p = subprocess.Popen("cat ../../inputs/16v_graphs.in | ../../build/ece650-prj -o -n 16 -l > 16_results.txt".format(run), shell=True)
    else:
        p = subprocess.Popen("cat ../../inputs/16v_graphs.in | ../../build/ece650-prj -o -n 16 -l".format(run), shell=True)
    processes.append(p)
    p.wait()
