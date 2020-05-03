# Single Cell Random Drawing

This python package will enable for users to reduce the size of input scRNAseq matrix by random selection of a given number of samples within pre-defined clusters and averaging the gene expression value of the chosen cells.

# Input
  1. Expression matrix of scRNAseq (gene by cells)
  2. Metadata (cell ids and cluster or cell type info)
  3. For visualization, pre-calculated tSNE or UMAP coordinates can be tossed along with metadata

# Returns
  1. shrunken matrix
  2. shrunken metadata
  3. cell.ids of randomly selected cells
  4. tSNE plot, if the coordinates were given.

# The benefit of downsizing cells with averaging gene exprssion values?
  1. downsizing itself reduce the calculation burden --> reducing calculation time
  2. Increase the resolution of differential gene expressin.

(e.g. assume that you have 400 cells in cluster 1 of your scRNAseq data, and if you set the number of cells to be chosen as 20, then 20 cells from cluster 1 of your data will be randomly and repeatedly selected with no replacement. This process will downsize the cluster 1 from 400 cells to 20 cells with better gene expression resolution.)
