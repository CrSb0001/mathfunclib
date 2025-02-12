from polynomial import poly_val
from math import sqrt

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

def identity(mat,val=1):
    '''
    The identity matrix * val

    :param mat: The size of the identity matrix to generate
    :param val: Optional with default 1, val to replace row[x] with.
    '''
    if type(mat)!=int or type(val)!=int:
        return "Both the required parameter and the optional parameter must be integers."

    matrix=[]
    for x in range(mat):
        row = [0]*mat
        row[x] = val
        matrix.append(row)
    return matrix

def fillmatrix(size,val=0):
    '''
    Fills with a matrix with a value:

    :param size: Tuple denoting the size of the matrix (width, height)
    :param val: Value to fill the matrix with.

    :returns: Matrix
    '''
    if type(size)!=tuple:
        return '[size] must be a tuple.'
    if type(val)!=int:
        return '[val] must be an integer.'
    
    return [[val]*size[1] for _ in range(size[0])]

def matrix_add(A,B,subtract=False):
    '''
    Adds two matrices of the same size.

    :param A: Matrix
    :param B: Matrix
    :param subtract: Optional parameter, subtracts the two matrices
                     if True.
    '''
    if type(A)!=list or type(B)!=list:
        return "Both matrices must be lists."
    if subtract!=False and subtract!=True:
        return f"Optional parameter [subtract] must be one of [True] or [False].\nGot {subtract} instead."
    
    m0,n0,m1,n1=len(A),len(A[0]),len(B),len(B[0])
    for i in range(1,len(A)):
        if len(A[0])!=len(A[i]):
            return "Matrix A must be a proper matrix."
    for i in range(1,len(B)):
        if len(B[0])!=len(B[i]):
            return "Matrix B must be a proper matrix."
    
    if m0!=m1 or n0!=n1:
        return "Matrices are not the same size."
    else:
        for x0 in range(m0):
            for x1 in range(n0):
                if subtract:
                    A[x0][x1] -= B[x0][x1]
                else:
                    A[x0][x1] += B[x0][x1]
    return A

def mat_mul(A,B):
    '''
    Multiples two matrices together.
    
    If [A] and [B] are both n*n matrices, the result will
    be an n*n matrix.
    If [A] is r*s and [B] is s*t, then the result will be
    an r*t matrix.
    Else, we cannot multiply the matrices together.

    :param A: Matrix
    :param B: Matrix

    :returns: Matrix A*B
    '''
    if type(A)!=list or type(B)!=list:
        return "Both parameters [A] and [B] must be matrices."
    for i in range(1,len(A)):
        if len(A[0])!=len(A[i]):
            return "Matrix [A] must be a proper matrix."
    for i in range(1,len(B)):
        if len(B[0])!=len(B[i]):
            return "Matrix [B] must be a proper matrix."
    
    m0,n0,m1,n1=len(A),len(A[0]),len(B),len(B[0])
    if n0!=m1:
        return "Cannot multiply matrices."
    
    matrix=fillmatrix((m0,n1))
    for row in range(m0):
        for col in range(n1):
            for itr in range(len(B)):
                matrix[row][col] += A[row][itr]*B[itr][col]
    return matrix

def mat_pow(mat,pow):
    '''
    Matrix exponentiation.

    :param mat: Matrix
    :param pow: Power to raise the matrix to. Must be an integer.

    :returns: Matrix mat**pow.
    '''
    if type(mat)!=list:
        return "Parameter [mat] must be a matrix."
    if type(pow)!=int or pow<=0:
        return f"Either parameter [pow] is not of type 'int', or\nis an integer that could potentially return\n an incorrect result."
    for i in range(1,len(mat)):
        if len(mat[0])!=len(mat[i]):
            return "Parameter [mat] must be a proper matrix."
    if len(mat[0])!=len(mat):
        return "Parameter [mat] must be a square matrix."
    
    mat_res=mat
    for bit in bin(pow)[3:]:
        mat_res=mat_mul(mat_res,mat_res)
        if bit=='1':
            mat_res=mat_mul(mat_res,mat)
    return mat_res

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
    if type(int_result)!=bool or (int_result not in [True,False]):
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

    Helper function for inverse, solve and pseudo_inv.
    '''
    if type(matrix)!=list:
        return f"Input [matrix] must be a list, got type \"{type(matrix)}\" instead."
    if aug_part!=None:
        if type(aug_part)!=list:
            return f"Optional param [aug_part] must be a list if not [None], got type \"{type(aug_part)}\" instead."
        else:
            matrix=concatenate(matrix,aug_part)
    if type(res_round)!=int:
        return f"Optional param [res_round] expected to have type [int], got type \"{type(res_round)}\" instead."
    
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

def solve(M,b,req_prec=0):
    '''
    Finds the solution, x, to the equation Mx==b

    :param M: Matrix
    :param b: Vector
    :param req_prec: Optional parameter for required precision. Default is 0.

    :returns: The vector x, or an error message.
    '''
    if type(M)!=list:
        return f"Type [list] expected for matrix [M], found \"{type(M)}\" instead."
    if type(b)!=list:
        return f"Type [list] expected for vector [b], found \"{type(b)}\" instead."
    if len(b[0])>1:
        return f"[b] must be a vector, found length {len(b[0])} instead"
    for i in range(1,len(b)):
        if len(b[0])!=len(b[i]):
            return "[b] must be a proper vector."
    
    m,n=len(M),len(M[0])
    if len(M)!=len(b):
        return "Impossible to solve."
    if gauss_jordan_elim(M,b,None,req_prec):
        return [M[x][n:]for x in range(m)]
    else:
        return "No solution or infinite solutions are possible."

def inverse(matrix,req_prec=0):
    '''
    Finds the inverse of a matrix by performing Gauss-Jordan Elimination.

    :param matrix: The matrix that is to be inverted.
    :param req_prec: Optional parameter for required precision in the case
                     of floats, default 0.

    :returns: Inverted matrix if the matrix has an inverse.
    '''
    if type(matrix)!=list:
        return f"Matrix must be of type [list], got type [{type(matrix)}] instead."
    if type(req_prec)!=int:
        return f"Parameter [req_prec] must be of type [int], got type [{type(req_prec)}] instead."
    
    for i in range(len(matrix)):
        if len(matrix)!=len(matrix[i]):
            return "Matrix must be a square matrix."
    
    m=len(matrix)
    if gauss_jordan_elim(matrix,identity(m),req_prec):
        return [matrix[x][m:] for x in range(m)]
    else:
        return "Matrix does not have an inverse."

def transpose(matrix):
    '''
    Finds the transpose of a matrix.
    '''
    if type(matrix)!=list:
        return f"Matrix must be of type [list], got type [{type(matrix)}] instead."
    for i in range(1,len(matrix)):
        if len(matrix[i])!=len(matrix[0]):
            return "All rows of [matrix] must have the same length."
    
    transpose=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transpose[j][i]=matrix[i][j]
    return transpose

def pseudo_inv(matrix,req_prec=0):
    '''
    Finds the pseudoinverse of a matrix ((transpose(A)*A)^{-1})*transpose(A) == A^+.
    If a square matrix is input, then it uses inverse() to find it.
    '''
    if type(matrix)!=list:
        return f"Matrix must be of type [list], got type [{type(matrix)}] instead."
    if type(req_prec)!=int:
        return f"Parameter [req_prec] must be of type [int], got type [{type(req_prec)}] instead."
    for i in range(1,len(matrix)):
        if len(matrix[i])!=len(matrix[0]):
            return "All rows of [matrix] must have the same length."
    
    if len(matrix)==len(matrix[0]):
        return inverse(matrix,req_prec)
    else:
        temp_mat = mat_mul(transpose(matrix),matrix)
        if gauss_jordan_elim(temp_mat,identity(len(temp_mat)),req_prec):
            m=len(temp_mat)
            temp_mat=[temp_mat[x][m:] for x in range(m)] # temp_mat == inverse(transpose(matrix)*matrix)
            return mat_mul(temp_mat,transpose(matrix))
        else:
            return "Matrix does not have a pseudoinverse."

def get_mat_minor(matrix,i,j):
    '''
    Used for finding the cofactor matrix.
    '''
    return ((-1)**(i+j))*determinant([row[:j]+row[j+1:]for row in (matrix[:i]+matrix[i+1:])])

def characteristic_poly(matrix,req_prec=2,to_poly=False):
    '''
    Returns the characteristic polynomial of a matrix.
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be a list."
    if type(req_prec)!=int:
        return "Parameter [req_prec] must be an integer."
    if to_poly not in [True, False]:
        return "Parameter [to_poly] must either be True or False. By default this is False."
    for i in range(1,len(matrix)):
        if len(matrix[0])!=len(matrix[i]):
            return "All rows of [matrix] must have the same length."
    if len(matrix)!=len(matrix[0]):
        return "[matrix] must be a square matrix."
    
    _len = len(matrix)
    iden = identity(_len)
    
    # Init polynomial coefficients
    coefficients = [0] * (_len + 1)
    coefficients[-1] = determinant(matrix,False,req_prec)*((-1)**(_len))
    
    # Find the coefficients
    for k in range(1,_len+1):
        sub_mat = [[matrix[i][j] - (x if i == j else 0) for j in range(_len)] for i in range(_len)]
        coefficients[-k-1] = determinant(sub_mat,False,req_prec) * ((-1)**(_len-k))
    
    # Construct the polynomial if to_poly == True
    if to_poly:
        return poly_val(coefficients,None)
    return coefficients

def cofactor_mat(matrix):
    '''
    Returns the matrix of cofactors of a matrix
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be a list."
    for i in range(1,len(matrix)):
        if len(matrix[0])!=len(matrix[i]):
            return "Matrix must have the length of all rows equal to each other."
    if len(matrix)!=len(matrix[0]):
        return "Matrix must be square."
    
    return [[get_mat_minor(matrix,i,j) for i in range(len(matrix))] for j in range(len(matrix))]

def adjugate_mat(matrix):
    '''
    Returns the adjugate of a matrix, that is transpose(C),
    where C == cofactor_mat(matrix)
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be a list."
    for i in range(1,len(matrix)):
        if len(matrix[0])!=len(matrix[i]):
            return "Matrix must have the length of all rows equal to each other."
    if len(matrix)!=len(matrix[0]):
        return "Matrix must be square."
    
    return transpose(cofactor_mat(matrix))

# ____________________________________________________________________________ #
#| Stuff with vectors, some needed as setup for the QR factorization function |#
#|____________________________________________________________________________|#

def dot_prod(v1,v2):
    return sum(x*y for x,y in zip(v1,v2))

def vec_add(v1,v2):
    return [x+y for x,y in zip(v1,v2)]

def vec_subt(v1,v2):
    return [x-y for x,y in zip(v1,v2)]

def scalar_mult(scalar,vector):
    return [scalar * x for x in vector]

def vec_norm(v):
    return sqrt(sum(x*x for x in v))

# ________________________________ #
#| Matrix decomposition functions |#
#|________________________________|#

def LU_decomp_mat(matrix,int_res=False):
    '''
    Returns the LU decomposition of a square matrix.
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be a list."
    for i in range(len(matrix)):
        if len(matrix)!=len(matrix[i]):
            return "Matrix must be square as implementhing this for nonsquare matrices is going to be difficult."
    
    n,L,U = len(matrix),[[0.0]*n for _ in range(n)],[[0.0]*n for _ in range(n)]
    for i in range(n):
        # Upper Triangular
        for k in range(i,n):
            _sum = 0.0
            for j in range(i):
                _sum += L[i][j]*U[j][k]
            U[i][k] = matrix[i][k] - _sum
        
        # Lower Triangular
        for k in range(i,n):
            if i == k:
                L[i][i] == 1.0
            else:
                _sum = 0.0
                for j in range(i):
                    _sum += L[k][j]*U[j][i]
                L[k][i] = (matrix[k][i] - sum) / U[j][i]
    if int_res:
        L = [[int(L[i][j]) for j in range(len(L))] for i in range(len(L))]
        U = [[int(U[i][j]) for j in range(len(U))] for i in range(len(U))]
    return L,U

def gram_schmidt(matrix,int_res):
    '''
    Uses the Gram-Schmidt process to find the QR decomposition
    of a matrix.
    '''
    if type(matrix)!=list:
        return "Parameter [matrix] must be a list."
    if int_res not in [True,False]:
        return f"[int_res] must be one of True or False, got {int_res} instead."
    for i in range(1,len(matrix)):
        if len(matrix[0])!=len(matrix[i]):
            return "Matrix must be a proper square matrix."
    
    n,m = len(matrix),len(matrix[0])
    Q,R = [[0.0]*m for _ in range(n)], [[0.0]*m for _ in range(m)]
    for j in range(m):
        v = [matrix[i][j] for i in range(n)]
        for i in range(j):
            q = [Q[k][i] for k in range(n)]
            R[i][j] = dot_prod(q,v)
            v = vec_subt(v,scalar_mult(R[i][j],q))
        R[j][j] = vec_norm(v)
        q = scalar_mult(1/R[j][j],v)
        
        for i in range(n):
            Q[i][j] = q[i]
    
    if int_res:
        Q = [[int(Q[i][j]) for j in range(len(Q[0]))]for i in range(len(Q))]
        R = [[int(R[i][j]) for j in range(len(R[0]))]for i in range(len(R))]
    return Q,R
