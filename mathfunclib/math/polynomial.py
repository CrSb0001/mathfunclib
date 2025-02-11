import typing

def poly_val(_list,x_int=0):
    '''
    Evaluates a polynomial at a specific point.
    If no value is given for x_int, then it defaults to 0.
    
    You can alternatively set x_int==None to simply output
    the polynomial.
    '''
    if type(_list)!=list:
        return f"Parameter [_list] must be a list, got type \"{type(_list)}\" instead."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All values of parameter [_list[ must be integers."
    if type(x_int)!=int and x_int!=None:
        return "Parameter [x_int] must be an integer if not None."
    
    if x_int==None:
        _str=''
        for i in range(len(_list)):
            if i!=len(_list)-1:
                if _list[i]==1:
                    _str+= f'(x ** {len(_list)-1-i}) + '
                elif _list[i]==0:
                    continue
                else:
                    _str+=f'{_list[i]} * (x ** {len(_list)-1-i}) + '
            else:
                _str+=f'{_list[i]}'
        return _str
    else:
        res=0
        for i in range(len(_list)):
            res+=_list[i]*(x_int**(len(_list)-1-i))
        return res

def poly_deriv(_list):
    '''
    Takes a list of elements representing the
    coefficients of a polynomial and takes its
    derivative.
    
    For example the list [1,0,9,6,7,1,3,0,2]
    represents the polynomial
    ```
    x**8 + 9*(x**6) + 6*(x**5) + 7*(x**4) + x**3 + 3*(x**2) + 2
    ```
    and so its derivative is
    ```
    8*(x**7) + 54*(x**5) + 30*(x**4) + 28*(x**3) + 3*(x**2) + 6*x
    ```
    '''
    if type(_list)!=list:
        return f"Parameter [_list] must be a list, got type \"{type(_list)}\" instead."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All values of parameter [_list] must be integers."
    
    arr = []
    for i in range(len(_list)-1):
        arr.append(_list[i]*(len(_list)-i-1))
    return arr

def poly_deriv_pt(_list,x=0):
    '''
    Takes a list of elements representing the
    coefficients of a polynomial and takes its
    derivative at a point. By default, this is
    being taken at x==0.
    
    If the optional parameter [x] is equal to None,
    then we just output a representation of its
    derivative using poly_val().
    '''
    if type(_list)!=list:
        return f"Parameter [_list] must be a list, got type \"{type(_list)}\" instead."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All values of parameter [_list] must be integers."
    if type(x)!=int and x!=None:
        return "Parameter [x] must be an integer if not None."
    
    if x==None:
        return poly_val(poly_deriv(_list),x_int=None)
    else:
        return poly_val(poly_deriv(_list),x)

def poly_int(_list,k=0,req_prec=0):
    '''
    Returns the antiderivative of the coefficients
    of a polynomial represented by a list.

    Parameter [k] is by default 0, but can be
    changed to be any number (float or integer) as
    desired.

    Parameter [req_prec) is by default 0, and represents
    the required precision for each element of the antiderivative.
    If this is equal to 0, we take each element of _list and make it
    and integer.
    '''
