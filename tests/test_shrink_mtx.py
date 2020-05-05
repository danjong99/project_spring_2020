
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from bk_packages.shrink_mtx import rand_draw

#### Read Meta Files - read as list of lists
meta = []
with open("tests/metatable.txt") as f_obj:
     for line in f_obj:
        res = line.replace('"','').strip('\n').split('\t')
        meta.append(res)
    
### Insert one element in the 1th list of the meta data
meta[0].insert(0,'rowname')
    
### Read matrix file - read as list of lists
mtx = []
with open("tests/exprs_mtx.txt") as f_obj:
    for line in f_obj:
        res = line.replace('"','').strip('\n').split('\t')
        mtx.append(res)
    
### Insert one element in the 1th list of the mtx
mtx[0].insert(0,'gene')

my_data = rand_draw(mtx=mtx, meta=meta, num_to_select=20)

def test_clustocell_dic_generator():
    my_data.A_clustocell_dic_generator()
    obs = []
    for i in range(0, len(my_data.meta_by_cluster)):
        obs.append(len(my_data.meta_by_cluster[i]))
    exp = [200,200,200,132,57,200,200,200,200,200,200,200,200]
    assert obs == exp

def test_clustocell_dic_generator():
    my_data.A_clustocell_dic_generator()
    obs = {}
    for k, v in my_data.meta_dic.items():
        obs[k] = len(v)
    exp = {'0': 200,'1': 200,'10': 200,'11': 132,'12': 57,'2': 200,'3': 200,'4': 200,'5': 200,'6': 200,'7': 200,'8': 200,'9': 200}
    assert obs == exp

def test_celltogene_dic_generator():
    my_data.B_celltogene_dic_generator()
    a = []
    for k in my_data.mtx_dic.keys():
        a.append(k)
    obs = {}
    obs[a[0]] = len(a[1:])
    exp = {'gene': 2389}
    assert obs == exp

def test_random_selector():
    my_data.C_random_selector(num_to_select=56)
    obs = []
    for k, v in my_data.dic_random_items.items():
        obs.append(len(v))
    exp = [56,56,56,32,56,56,56,32,56,56,56,32,56,56,20,56,1,56,56,56,32,56,56,56,
           32,56,56,56,32,56,56,56,32,56,56,56,32,56,56,56,32,56,56,56,32,56,56,56,32]
    assert obs == exp
