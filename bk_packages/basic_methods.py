
def unique(input_list):
    """Return unique value of the input list"""  
    try:
        # intilize a null list 
        unique_list = [] 
        # traverse for all elements 
        for x in input_list: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x)
        return(unique_list)
    except TypeError as detail:
        return ("int object is not iterable")

def t(mtx):
    """T-transform the Input Matrix"""
    try:
        if type(mtx) is str: #if the input is str, raise exception.
            raise Exception('Error: the input should be a list of lists.')
        
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        ## Execution code
        mtx_t = []
        for j in range(0, len(mtx[0])):
            mtx_t.append( [mtx[i][j] for i in range(0,len(mtx))] )
        return(mtx_t)
    
    except TypeError as detail: # Control TypeEorror.
        return ('Error: the input should be a list of lists.')
    except AssertionError as detail:
        return ('Error: length of the lists should be the same')

def convert_to_float(input_list):
    """Convert list of str to list of float"""
    try:
        list_float = [float(i) for i in input_list]
        return(list_float)
    except ValueError as detail:
        return ("input is not convertible to float.")

def rowSum(mtx):
    """Return all row-sums as a list"""
    try:
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        res = list()
        for j in range(0, len(mtx[0])): 
            tmp = 0
            for i in range(0, len(mtx)): 
                tmp = tmp + mtx[i][j]
            res.append(tmp)
        return(res)
    
    except AssertionError as detail:
        return ('Length of lists is irregular or input format is wrong.')
    except TypeError as detail:
        return ('Undefined operand type')

def rowMean(mtx):
    """Return all row-sums as a list"""
    try:
        for i in range(0, len(mtx)):
            assert len(mtx[i]) == len(mtx[i-1]) # check whether each list has the same length.
        
        res = list()
        for j in range(0, len(mtx[0])): 
            tmp = 0
            for i in range(0, len(mtx)): 
                tmp = tmp + mtx[i][j]
            res.append(tmp/len(mtx))
        return(res)
    
    except AssertionError as detail:
        return ('Length of lists is irregular or input format is wrong.')
    except TypeError as detail:
        return ('Undefined operand type')
