
from bk_packages.basic_methods import t, convert_to_float, unique, rowSum, rowMean

def test_t():
    input_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    obs = t(input_list)
    exp = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    assert obs == exp

def test_convertTofloat():
    input_list = ['1','2','3','4','5','6','7','8','9','10']
    obs = convert_to_float(input_list)
    exp = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    assert obs == exp

def test_unique():
    input_list = [1,1,1,2,2,2,3,3,4,4,5,5,6,6,7,8,9,9,9,9,9,9,10]
    obs = unique(input_list)
    exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert obs == exp

def test_rowSum():
    input_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    obs = rowSum(input_list)
    exp = [22, 26, 30]
    assert obs == exp

def test_rowMean():
    input_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    obs = rowMean(input_list)
    exp = [5.5, 6.5, 7.5]
    assert obs == exp
