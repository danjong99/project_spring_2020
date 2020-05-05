# Single Cell Random Drawing

This python package will enable for users to reduce the size of input scRNAseq matrix by random selection of a given number of samples within pre-defined clusters and averaging the gene expression value of the chosen cells.

# Import
  - from bk_packages.shrink_mtx import rand_draw

# Input
  1. Expression matrix of scRNAseq (gene by cells) - mtx
  2. Metadata (cell ids and cluster or cell type info) - meta
  3. For visualization, pre-calculated tSNE or UMAP coordinates can be tossed along with metadata

# Description

  1. Using well-built packages e.g. numpy and pandas are avoided as much as possible because this is a learning course.
     However, numpy, pandas, matplotlib and seaborn used for visualization of input and output.
  2. I used class, which seems redundant in this case, for practice. Version w/o class is in old code folder ( but not complete form ).
  3. How it works.
     'rand_draw' class has 4 essential methods (annotated by Alphabet A-D) to accomplish the intended task 
      and 3 additional methods for reports.
        - First, generate an object (obj = rand_draw(mtx, meta, num_to_select))
        - you should perform obj.A-(), .B-(), .C-() and .D-() in order.
        - obj.E-() is for brief report of result.
        - obj.tSNE_intput() / .tSNE_output() return original/shrunken tSNE plot, repectively,
          if the coordinates were given.
    
# The benefit of downsizing cells with averaging the exprssion levels of gene?
  1. downsizing itself reduce the calculation burden --> reducing calculation time
  2. Increase the resolution of differential gene expressin.

(e.g. assume that you have 400 cells in cluster 1 of your scRNAseq data, and if you set the number of cells to be chosen as 20, then 20 cells from cluster 1 of your data will be randomly and repeatedly selected with no replacement. This process will downsize the cluster 1 from 400 cells to 20 cells with better gene expression resolution.)
