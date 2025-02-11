import typing

# Really I do enjoy (and prefer!) using numpy, but if anything I'm only making this so it's easier to see how exactly these functions work.

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
            return "All values of parameter [_list] must be integers."
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

def poly_int(_list,k=0,req_prec=0,to_poly=False):
    '''
    Returns the antiderivative of the coefficients
    of a polynomial represented by a list.
    
    Parameter [k] is by default 0, but can be
    changed to be any number (float or integer) as
    desired.
    
    Parameter [req_prec) is by default 0, and represents
    the required precision for each element of the antiderivative.
    If this is equal to 0, we take each element of _list and make it
    and integer. Of course, this is not necessarily recommended.
    '''
    if type(_list)!=list:
        return f"Parameter [_list] must be a list, got type \"{type(_list)}\" instead."
    for i in range(len(_list)):
        if type(_list[i])!=int and type(_list[i])!=float:
            return "All values of parameter [_list] must either be an integer or a float."
    if (type(k)!=int and type(k)!=float) or type(req_prec)!=int:
        return f"Optional parameter [k] must either be an integer or a float.\nOptional parameter [req_prec] must be an integer.\nGot \"{type(k)}\" and \"{type(req_prec)}\" for [k] and [req_prec] instead, respecitively."
    if to_poly not in [True,False]:
        return f"Parameter [to_poly] must be either True or False, got {to_poly} instead."
    if req_prec<0:
        return "Required precision of the output cannot be less than 0."
    
    arr = []
    for i in range(len(_list)):
        if req_prec==0:
            arr.append(_list[i]//(len(_list)-i))
        else:
            arr.append(round(_list[i]/(len(_list)-i),req_prec))
    if req_prec==0:
        arr.append(int(k))
    else:
        arr.append(round(k,req_prec))
    if to_poly:
        return poly_val(arr,None)

def poly_mul(_list1,_list2,to_poly=False):
    '''
    Takes two lists representing the coefficients
    of their corresponding polynomials and multiplies
    them together.
    
    You can also set to_poly=True to output the polynomial
    using poly_val(), although by default is set to False.
    '''
    if type(_list1)!=list or type(_list2)!=list:
        return f"Both lists [_list1] and [_list2] must be of type list,\ngot {type(_list1)} for _list1 and {type(_list2)} for _list2 instead."
    for i in range(len(_list1)):
        if type(_list1[i])!=int:
            return "All values in [_list1] must be integers."
    for i in range(len(_list2)):
        if type(_list2[i])!=int:
            return "All values in [_list2] must be integers."
    if to_poly not in [True,False]:
        return f"Parameter [to_poly] must be one of True or False, got {to_poly} instead."
    
    res=[0]*(len(_list1)+len(_list2)-1)
    for i1,j1 in enumerate(s1):
        for i2,j2 in enumerate(s2):
            res[i1+i2]+=j1*j2
    if to_poly:
        return poly_val(res,None)
    return res

def poly_add(_list1,_list2,to_poly=False):
    '''
    Takes two lists representing the coefficients
    of the corresponding polynomials and adds them together.
    
    You can also set to_poly=True to output the polynomial
    using poly_val(), although by default is set to False.
    '''
    if type(_list1)!=list or type(_list2)!=list:
        return f"Both lists [_list1] and [_list2] must be of type list,\ngot {type(_list1)} for _list1 and {type(_list2)} for _list2 instead."
    for i in range(len(_list1)):
        if type(_list1[i])!=int:
            return "All values in [_list1] must be integers."
    for i in range(len(_list2)):
        if type(_list2[i])!=int:
            return "All values in [_list2] must be integers."
    if to_poly not in [True,False]:
        return f"Parameter [to_poly] must be one of True or False, got {to_poly} instead."
    
    _min=min(len(_list1),len(_list2))
    res=[0]*max(len(_list1),len(_list2))
    if _min==len(_list1):
        for i in range(len(res)-_min):
            res[i]=_list2[i]
        for i in range(len(_list2)-len(res)+_min):
            res[len(res)-1-i]=_list1[len(_list1)-1-i]+_list2[len(_list2)-1-i]
    else:
        for i in range(len(res)-_min):
            res[i]=_list1[i]
        for i in range(len(_list1)-len(res)+_min):
            res[len(res)-1-i]=_list1[len(_list1)-1-i]+_list2[len(list2)-1-i]
    if to_poly:
        return poly_val(res,None)
    return res

def poly_sub(_list1,_list2,to_poly=False):
    '''
    Basically the same as poly_add, except now
    we're doing subtraction.
    
    Note that in general, a-b != b-a, so the order
    in which you put the polynomials in does matter in fact.
    
    As always, you can also set to_poly=True to output the polynomial
    using poly_val(), although by default is set to False.
    '''
    if type(_list1)!=list or type(_list2)!=list:
        return f"Both lists [_list1] and [_list2] must be of type list,\ngot {type(_list1)} for _list1 and {type(_list2)} for _list2 instead."
    for i in range(len(_list1)):
        if type(_list1[i])!=int:
            return "All values in [_list1] must be integers."
    for i in range(len(_list2)):
        if type(_list2[i])!=int:
            return "All values in [_list2] must be integers."
    if to_poly not in [True,False]:
        return f"Parameter [to_poly] must be one of True or False, got {to_poly} instead."
    
    _min=min(len(_list1),len(_list2))
    res=[0]*max(len(_list1),len(_list2))
    if _min==len(_list1):
        for i in range(len(res)-_min):
            res[i]=-_list2[i]
        for i in range(len(_list2)-len(res)+_min):
            res[len(res)-1-i]=_list1[len(_list1)-1-i]-_list2[len(_list2)-1-i]
    else:
        for i in range(len(res)-_min):
            res[i]=_list1[i]
        for i in range(len(_list1)-len(res)+_min):
            res[len(res)-1-i]=_list1[len(_list1)-1-i]-_list2[len(list2)-1-i]
    if to_poly:
        return poly_val(res,None)
    return res

def poly_degree(_list):
    '''
    Returns the degree of the polynomial
    '''
    if type(_list)!=list:
        return f"Parameter [_list] must be a list, got type \"{type(_list)}\" instead."
    for i in range(len(_list)):
        if type(_list[i])!=int and type(_list[i])!=float:
            return "The elements of parameter [_list] must have float values if not integers."
    
    return len(_list)
