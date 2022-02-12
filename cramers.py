import copy


def solve_matrix(m):
    '''
    input: m - matrix (2d array,  where n rows = n columns - 1)
    output: ans - solved value of the matrix
    '''
    num=[]
    for i in range(2):
        for j in range(len(m[0])):
            num.append(j)
    msum = 0
    msub = 0
    for i in range(len(m)):
        mul_f_sum = 1
        mul_f_sub = 1
        for j in range(len(m[0])):
            mul_f_sum *= m[j][num[i + j]]
            mul_f_sub *= m[-j][num[i + j]]
        msum += mul_f_sum
        msub += mul_f_sub
    ans = msum - msub
    return ans


def check_system(matrix):
    matrix_len = len(matrix)
    for elem_len in list(map(len, matrix)):
        if matrix_len +1 != elem_len:
            raise ValueError('invalid format of matrix')


def cramers_system(matrix):
    
    check_system(matrix)
    
    mlen = len(matrix)
    melem = mlen + 1
    ans_col = [row[-1] for row in matrix]
    matrix_coef = [row[:-1] for row in matrix]
    
    matrixes = {}
    for matrix_n in range(mlen):
        temp = copy.deepcopy(matrix_coef)
        for i, row in enumerate(temp):
            row[matrix_n] = ans_col[i]
        matrixes[matrix_n] = temp  

    delta = solve_matrix(matrix_coef)
    if delta == 0:
        raise ValueError('delta of system = 0')
    
    ans = []
    for i in matrixes.keys():
        ans.append(solve_matrix(matrixes[i]) / delta)
    
    return ans