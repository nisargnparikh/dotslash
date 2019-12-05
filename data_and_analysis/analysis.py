#!/usr/bin/python3

import os
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

path = os.path.join('data', '5-10-15_CNF-SAT-VC.csv')
df = pd.read_csv(path, index_col=None, )

computed_sizes = defaultdict(list)

path = os.path.join('data', 'ALL_results.txt')
with open(path, 'r') as f:
    for line in f:
        algo, res = [x.strip() for x in line.split(':')]
        res = res.split(',')
        computed_sizes[algo].append(len(res))   

vertices = [5] * 10 + [10]*10 + [15]*10
cnf_res = np.array(computed_sizes['CNF-SAT-VC'])
approx_1_res = np.array(computed_sizes['APPROX-VC-1'])
approx_2_res = np.array(computed_sizes['APPROX-VC-2'])

data = {'vertices': vertices, 'CNFSAT_res': cnf_res, 'Approx1_res': approx_1_res, 'Approx2_res': approx_2_res}
df = pd.DataFrame(data=data, index=data['vertices'])


cnf_AR = cnf_res / cnf_res
vc1_AR = approx_1_res / cnf_res
vc2_AR = approx_2_res / cnf_res

avg_vc1_AR = np.mean(vc1_AR)
avg_vc2_AR = np.mean(vc2_AR)

data = {'vertices': vertices, 'CNFSAT': cnf_AR, 'Approx1': vc1_AR, 'Approx2': vc2_AR}
df = pd.DataFrame(data=data, index=data['vertices'])
df2 = df.groupby(['vertices']).mean()
df3 = df2.T

def f(x):
    d = {}
    d['a_sum'] = x['a'].sum()
    d['a_max'] = x['a'].max()
    d['b_mean'] = x['b'].mean()
    d['c_d_prodsum'] = (x['c'] * x['d']).sum()
    return pd.Series(d, index=['a_sum', 'a_max', 'b_mean', 'c_d_prodsum'])

df2 = df.groupby('vertices').apply(f)


sns.barplot(x=df3.index, y=df3[5,10], data=df3)
plt.show()
