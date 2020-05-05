
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from bk_packages.basic_methods import *
import random
import math
from bk_packages.basic_methods import unique, t, convert_to_float, rowMean

class rand_draw():
    """A simple way to visualize the results"""

    def __init__(self, mtx, meta, num_to_select=20):
        
        """Initialize object's attributes"""
        
        self.mtx = mtx
        self.meta = meta
        self.num_to_select = num_to_select
        
        self.meta_by_cluster = []
        self.meta_dic = {}
        self.mtx_dic = {}
        self.dic_random_items = {}
        self.mtx_small = {}
        
    def A_clustocell_dic_generator(self):
        
        """Return {cluster:cell.ids} dictionary """
        
        temp = [self.meta[i][2] for i in range(0,len(self.meta))] # extract cell cluster info
        unique_cluster = unique(temp[1:])         # take unique cluster info
        unique_cluster = sorted(unique_cluster)

        ## group cell.ids based on their cluster
        for cluster in unique_cluster:
            index = [i for i, n in enumerate(temp) if n == cluster] # extract the indices of rows in a given cluster
            a = [self.meta[i][1:3] for i in index] # using the indices, extract cell.id and assigned cluster info.
            self.meta_by_cluster.append(a)
    
        # convert the list acquired above to dictionary with the cluster as keys
        for j in range(0, len(unique_cluster)):
            self.meta_dic[ self.meta_by_cluster[j][0][1] ] = [ self.meta_by_cluster[j][i][0] for i in range(0, len(self.meta_by_cluster[j]))]
    
    def B_celltogene_dic_generator(self):
        """Apply T-transformation and convert the list of lists to Dictionary"""
        """with cell.id as keys and gene expression as value"""
        mtx_t = t(self.mtx)
        for line in mtx_t:
            self.mtx_dic[line[0]] = line[1:]
    
    def C_random_selector(self, num_to_select = None):
        """Random selection of cell.ids from each cluster"""
            
        if num_to_select != None:
            if isinstance(num_to_select, int):
                self.num_to_select = num_to_select
            else:
                raise Exception('Error: "num_to_select" undefined type')
                return 0
        
        self.dic_random_items = {} # reset dic_random_items
        for key in self.meta_dic.keys():
                        
            clust_cell_ids = self.meta_dic[key].copy()

            # determine the number of cycle to run in the following loop.
            if len(self.meta_dic[key]) < self.num_to_select:
                print("Number of items to select exceeds the number of items in the list.")
                print("Remember this is random selection without replacement.")
                cycle_to_run = math.floor(len(self.meta_dic[key])/self.num_to_select)
            elif len(self.meta_dic[key])%self.num_to_select == 0:
                cycle_to_run = int(len(self.meta_dic[key])/self.num_to_select)
            else:
                cycle_to_run = math.ceil(len(self.meta_dic[key])/self.num_to_select)

            for i in range(0, cycle_to_run): # random sampling from the given list without replacement
                if len(clust_cell_ids) > self.num_to_select:
                    a = random.sample(clust_cell_ids, self.num_to_select)
                    self.dic_random_items[ a[0] ] = a  # takes the first cell.id among selected ones as a key.
                    [clust_cell_ids.remove(a[i]) for i in range(0,len(a))] # selected cell.ids are removed from the dic.
                elif len(clust_cell_ids) < self.num_to_select: # the remaining cells are taken 
                    a = clust_cell_ids
                    self.dic_random_items[ a[0] ] = a
    
    def D_avg_gene(self):
        
        """Average gene expression values by defined rowMean fuction"""
        
        a = self.mtx_dic['gene'].copy()
        self.mtx_small['gene'] = a
    
        for key, values in self.dic_random_items.items():
            temp = []
            a = []
            for value in values:
                a = self.mtx_dic[ value ].copy()
                temp.append(convert_to_float(a))
            self.mtx_small[ key ] = rowMean(temp)
    
        #[v.insert(0,k) for k, v in mtx_small.items()]
        #temp_2 = [x for x in mtx_small.values()]    
        #temp = t(temp_2)
        #self.final_mtx = temp.copy()
    
    def E_briefing(self):
        
        """Briefly reports the result of random selection"""
        
        meta_by_clus_temp = []
        for i in range(0, len(self.meta_by_cluster)):
            for j in range(0, len(self.meta_by_cluster[i])):
                meta_by_clus_temp.append(self.meta_by_cluster[i][j])
        
        meta_by_clus_dic = {}
        for i in range(0, len(meta_by_clus_temp)):
            meta_by_clus_dic[ meta_by_clus_temp[i][0] ] = meta_by_clus_temp[i][1]

        for k, v in self.dic_random_items.items():
            print( "Key Cell ID: " + k + " - Assigned Cluster: " + str(meta_by_clus_dic[k]) + " - Number of Cell: " + str(len(v)))

        
    def tSNE_input(self):
        
        """Visualize tSNE cooridinates from original metadata"""
               
        temp = pd.DataFrame.from_dict(self.meta)
        temp.columns = [temp.iloc[0][i] for i in range(0,len(temp.columns))]
        pd_meta = temp.iloc[1:].copy()
        pd_meta[['tSNE_1','tSNE_2']] = pd_meta[['tSNE_1','tSNE_2']].astype(float)

        sns.lmplot(x='tSNE_1',
                   y='tSNE_2',
                   data=pd_meta,
                   fit_reg=False,
                   legend=True,
                   height=9,
                   hue='cluster',
                   scatter_kws={"s":200, "alpha":0.3})

        title = ('tSNE Plot of %s Mouse Colon Cells'% len(pd_meta))
        plt.title(title, weight='bold').set_fontsize('14')
        plt.xlabel('tSNE 1', weight='bold').set_fontsize('20')
        plt.ylabel('tSEN 2', weight='bold').set_fontsize('20')
    
    
    def tSNE_output(self):
        
        """Visualize tSNE cooridinates from shrunken metadata"""
        
        if bool(self.mtx_small):
            
            temp = pd.DataFrame.from_dict(self.meta)
            temp.columns = [temp.iloc[0][i] for i in range(0,len(temp.columns))]
            pd_meta = temp.iloc[1:].copy()

            pd_mtx_small = pd.DataFrame.from_dict(self.mtx_small)
            pd_meta.index = pd_meta['cell.id']
            df = pd_meta[ pd_meta.index.isin(pd_mtx_small.columns) ]       
            df[['tSNE_1','tSNE_2']] = df[['tSNE_1','tSNE_2']].astype(float)

            sns.lmplot(x='tSNE_1',
                       y='tSNE_2',
                       data=df,
                       fit_reg=False,
                       legend=True,
                       height=9,
                       hue='cluster',
                       scatter_kws={"s":200, "alpha":0.3})

            title = ('tSNE Plot of %s Mouse Colon Cells'% len(df))
            plt.title(title, weight='bold').set_fontsize('14')
            plt.xlabel('tSNE 1', weight='bold').set_fontsize('20')
            plt.ylabel('tSEN 2', weight='bold').set_fontsize('20')
        
        else:
            print("shrunken mtx is empy. A,B,C methods should be run.")
