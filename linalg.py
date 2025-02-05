import typing

def argmax(_list):
    '''
    Finds the argmax of a list.
    
    :param _list: A list
    :returns: The argmax of that list.
    '''
    if type(_list) != list:
        return f"Input must be a list. Got type \"{type(_list)}\" instead."
    f=lambda i: _list[i]
    return max(range(len(_list)),key=f)

def determinant(matrix,int_result=True,int_round=4):
    '''
    Returns the determinant of a square matrix.
    
    :param matrix:
    
    :returns: det(matrix). Is an integer if int_result (optional param)
                           is ommitted or set to true, else returns float
                           rounded to {int_round} decimal places (default 4).
    '''
    if type(matrix)!=list:
        return "Please input a list"
    if type(int_result)!=bool or int_result not in [True,False]:
        return f"Expected one of [True] or [False] for int_result, got '{int_result}' instead."
    if type(int_round)!=int:
        return f"Expected an integer type for int_round, got type\"{type(int_round)}\" instead."
    
    for i in range(len(matrix)):
        if len(matrix)!=len(matrix[i]) or len(matrix[0])!=len(matrix[i]):
            return "Please input a square matrix"
    
    h,k,det,m,n=0,0,1,len(matrix),len(matrix[0])
    
    while h<m and k<n:
        i_max = argmax([abs(matrix[i][k]) for i in range(h,m)])+h

        if matrix[i_max][k]==0:
            k+=1

        else:
            if h!=i_max:
                temp_row=matrix[i_max]
                matrix[i_max]=matrix[h]
                matrix[h]=temp_row
                det*=-1

            for i in range(h+1,m):
                f=matrix[i][k]/matrix[h][k]
                matrix[i][k]=0
                for j in range(k+1,n):
                    matrix[i][j]-=f*matrix[h][j]
            h+=1
            k+=1

    for i in range(m):
        det*=matrix[i][i]
    return int(det) if int_result else round(det,int_round)

def concat(A,B):
    '''
    Concatenates two lists, list A and list B.

    :param A: Matrix
    :param B: Matrix

    :returns: Matrix

    Helper function for inverse and solve.
    '''
    if type(A)!=list or type(B)!=list:
        return f"Both parameters must contain lists.\nCurrently, the type of A is \"{type(A)}\" and the type of B is \"{type(B)}\"."
    
    for i in range(1,len(A)):
        if len(A[0])!=len(A[i]):
            return f"Matrix A is not a proper matrix.\nFound len(A[{i}])=={len(A[i])} while len(A[0])=={len(A[0])}."
    for i in range(1,len(B)):
        if len(A[0])!=len(A[i]):
            return f"Matrix B is not a proper matrix.\nFound len(B[{i}])=={len(B[i])} while len(B[0])=={len(B[0])}."
    
    m1,m2=len(A),len(B)
    if m1!=m2:
        return "Cannot concatenate horizontally."
    
    for row in range(m1):
        A[row]+=B[row]
    
    return A

def gauss_jordan_elim(matrix,aug_part=None,res_round=4):
    '''
    Performs Gauss Jordan Elimination on the given matrix.

    :param matrix: The matrix to perform the algorithm on.
    
    :optional param aug_part: Will attach the argument onto the matrix
                              and then perform the algorithm.
    
    :optional param res_round: Gives desired amount of accuracy. Will
                               take the integer part of the argument if
                               set to 0.
    
    :returns: True if the operation was successful, False otherwise.

    Helper function for inverse and solve.
    '''
    if type(matrix)!=list:
        return f"Input [matrix] must be a list, got \"{type(matrix)}\" instead."
    if aug_part!=None:
        if type(aug_part)!=list:
            return f"Optional param [aug_part] must be a list if not [None], got \"{type(aug_part)}\" instead."
        else:
            matrix=concatenate(matrix,aug_part)
    if type(res_round)!=int:
        return f"Optional param [res_round] expected to have type [int], got \"{type(res_round)}\" instead."
    
    m,n,h,k = len(matrix),len(matrix[0]),0,0
    while h < m and k < n:
        i_max = argmax([abs(matrix[i][k]) for i in range(h, m)]) + h
        if matrix[i_max][k] == 0:
            k += 1
        else:
            if h != i_max:
                temp_row = matrix[i_max]
                matrix[i_max] = matrix[h]
                matrix[h] = temp_row
            for i in range(h + 1, m):
                f = matrix[i][k]/matrix[h][k]
                matrix[i][k] = 0
                for j in range(k + 1, n):
                    matrix[i][j] -= f*matrix[h][j]
            h += 1
            k += 1
    for y in range(m-1, -1, -1):
        t = matrix[y][y]
        if abs(t) < 10**(-10):
            return False
        for z in range(0,y):
            for x in range(n-1, y-1, -1):
                matrix[z][x] -= matrix[y][x] * matrix[z][y] / t
                if res_round!=0:
                    matrix[z][x] = round(matrix[z][x], res_round)
                else:
                    matrix[z][x]= int(matrix[z][x])
        matrix[y][y] /= t
        if res_round!=0:
            matrix[y][y] = round(matrix[y][y], res_round)
        else:
            matrix[y][y] = int(matrix[y][y])
        for x in range(m, n):
            matrix[y][x] /= t
            if res_round!=0:
                matrix[y][x] = round(matrix[y][x], res_round)
            else:
                matrix[y][x] = int(matrix[y][x])
    return True
