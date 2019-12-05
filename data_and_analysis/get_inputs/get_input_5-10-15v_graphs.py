#!/usr/bin/python3

import subprocess
import time

for run in range(0,10):
    print('Starting Run: ', run)
    print('================================================================\n\n')
    if run == 0:
        p = subprocess.Popen("cat ../../sample_inputs/5-10-15_graphs.txt | ../../build/ece650-prj -o -n 5-10-15 -l > 5-10-15_results.txt", shell=True)
    else:
        p = subprocess.Popen("cat ../../sample_inputs/5-10-15_graphs.txt | ../../build/ece650-prj -o -n 5-10-15", shell=True)
    p.wait()
    
