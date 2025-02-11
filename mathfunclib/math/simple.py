import typing
from math import gcd

def num_to_base(n,b,to_str=False):
    '''
    Takes an integer [n] and outputs it in base [b].
    Unary (base 1) is not supported, as well as any base greater than 36.

    :param n: The number that we are converting form base 10 to another base.
    :param b: The base that we are outputting in.
    :param to_str: Optional parameter if output as a string is required.
                   Recommended for large [n].

    :returns: The number [n] in base [b].
    '''
    NUM_TO_STR=['0','1','2','3','4','5','6','7','8','9']
    HIGH_BASE_LIST=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    _str=''
    
    if (type(n)!=int) or (type(b)!=int):
        return "All required parameters must be integers."
    if to_str!=False and to_str!=True:
        return f"Parameter [to_str] must be one of [True] or [False], got {to_str} instead."
    if n<0:
        return "Parameter [n] must be greater or equal to 0."
    if b<=1:
        return "The base [b] must be greater than 2."
    if b>36:
        return "The base [b] cannot be greater than 36."
    
    if n==0 or n==1:
        if to_str:
            return f'{n}'
        else:
            return [n]
    if b==10:
        if to_str:
            return str(n)
        else:
            return list(str(n))
    
    digits=[]
    while n!=0:
        digits.append(int(n%b))
        n//=b
    digits=digits[::-1]
    for i in range(len(digits)):
        if digits[i]<10:
            digits[i]=NUM_TO_STR[digits[i]]
        elif digits[i]>=10:
            digits[i]=HIGH_BASE_LIST[digits[i]-10]
    if to_str:
        _str.join(digits)
        return _str
    else:
        return digits

def mod_div(a,b,m):
    '''
    Finds a/b mod m
    
    :param a: Integer
    :param b: Integer
    :param m: Integer
    
    :returns: a/b mod m
    '''
    if (type(a)!=int) or (type(b)!= int) or (type(m)!=int):
        return "All parameters must be integers."
    try:
        inv=pow(b,-1,m)
    except ValueError:
        if a%b==0:
            answer = ((a%m)*b)//b
    else:
        a=a%m
        answer=(inv*a)%m
    return answer

def is_clockwise(a,b,c):
    '''
    Finds if three points [a] going to [b] going to [c] are in clockwise order.
    Is used in the convex hull algorithm.

    :param a: A tuple, representing a point in 2D
    :param b: A tuple, representing a point in 2D
    :param c: A tuple, representing a point in 2D

    :returns: Whether or not the three points are in clockwise order.
    '''
    if (type(a)!=tuple) or (type(b)!=tuple) or (type(c)!= tuple):
        return "All parameters must be tuples."
    
    ax,ay=a
    bx,by=b
    cx,cy=c
    if (cy-ay)*(bx-ax)<(by-ay)*(cx-ax):
        return True
    return False

def simp_euclid_alg(a,b):
    '''
    A simple implementation of the Euclidean Algorithm.

    :param a: Integer coefficient
    :param b: Integer coefficient

    :returns: The greatest common divisor between [a] and [b].
    '''
    if (type(a)!=int) or (type(b)!=int):
        return "All parameters must be integers."
    if (a<=0) or (b<=0):
        return "All parameters must be greater than 0."
    
    while b>0:
        a,b=b,a%b
    return a

def extended_euclid_alg(a,b):
    '''
    An implementation of the Extended Euclidean Algorithm.

    :param a: Integer coefficient.
    :param b: Integer coefficient.

    :returns: A tuple (g,s,t) where gcd(a,b) == g == as+bt
    '''
    if type(a)!=int or type(b)!=int:
        return "All parameters must be integers."
    
    old_r,r=a,b
    old_s,s=1,0
    while r!=0:
        q = old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
    if b!=0:
        bezout_t=(old_r-old_s*a)//b
    else:
        bezout_t=0
    return old_r,old_s,bezout_t

def lcm_list(_list):
    '''
    Finds the least common multiple of a list of integers.

    :param _list: A list of integers.

    :returns: The LCM of all of the integers.
    '''
    if type(_list)!=list:
        return "Parameter [_list] must be a list."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All elements of parameter [_list] must be integers."
    
    n=_list.sort()
    curr=n.pop(-1)
    while len(n)!=0:
        temp=n.pop(-1)
        curr=abs(curr*temp)//gcd(curr,temp)
    return curr

def bin_exp_mod(a,b,c,n,m=None):
    '''
    If (a+b*sqrt(c))^n (mod m) = x + y*sqrt(c), then this algorithm finds this
    using binary exponentiation.

    :param a: Integer coefficient on non-sqrt term.
    :param b: Integer coefficient of sqrt term.
    :param c: Integer coefficient inside sqrt term.
    :param n: Integer exponent.
    :param m: Integer coefficient of the modulus, optional.

    :returns: Tuple (x,y) such that (a+b*sqrt(c))^n (mod m) = x + y*sqrt(c)
    '''
    if type(a)!=int or type(b)!=int or type(c)!=int or type(n)!=int:
        return "All required parameters must be integers."
    if m!=None and type(m)!=int:
        return "Optional parameter [m] must be an integer if not [None]."
    if n<0 or m<=1:
        return "The exponent should be 1 or greater and the modulus should be greater than 1."
    
    if m==None:
        a_res,b_res=a,b
        for bit in bin(n)[3:]:
            a_res,b_res=a_res*a_res+c*b_res*b_res,2*a_res*b_res
            if bit=='1':
                a_res,b_res=a*a_res+b*c*b_res,b*a_res+a*b_res
    else:
        a_res,b_res=a,b
        for bit in bin(n)[3:]:
            a_res,b_res=(a_res*a_res+c*b_res*b_res)%m,(2*a_res*b_res)%m
            if bit=='1':
                a_res,b_res=(a*a_res+b*c*b_res)%m,(b*a_res+a*b_res)%m
    return a_res,b_res

def bisector_right(_list,goal,lo=0,hi=None):
    '''
    An implementation of bisect_right from the bisect module.
    This has been in Python since Python 3.9.

    :param _list: A list of integers.
    :param goal: An integer number.

    :returns: index i of _list such that _list[i-1] < goal < _list[i]
    '''
    if type(_list)!=list:
        return "Parameter [_list] must be a list."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All elements of _list must be integers."
    if type(goal)!=int:
        return "Parameter [goal] must be an integer."

    if lo<0:
        raise ValueError('Parameter [lo] must be a non_negative integer.')
    if hi is None:
        hi = len(_list)
    while lo<hi:
        mid=(lo+hi)//2
        if goal<_list[mid]:
            hi=mid
        else:
            lo=mid+1
    return lo

def bisector_left(_list,goal,lo=0,hi=None):
    '''
    An implementation of bisect_left form the bisect module.
    This has been in Python since Python 3.9.
    
    :param _list: A list of integers.
    :param goal: An integer number
    '''
    if type(_list)!=list:
        return "Parameter [_list] must be a list."
    for i in range(len(_list)):
        if type(_list[i])!=int:
            return "All elements of _list must be integers."
    if type(goal)!=int:
        return "Parameter [goal] must be an integer."
    
    if lo<0:
        raise ValueError('Parameter [lo] must be a non_negative integer')
    if hi is None:
        hi = len(_list)
    while lo<hi:
        mid = (lo+hi)//2
        if _list[mid]<goal:
            lo = mid+1
        else:
            hi = mid
    return lo

def insorter_right(_list,x,lo=0,hi=None):
    lo=bisector_right(_list,x,lo,hi)
    _list.insert(lo,x)

def insorter_left(_list,x,lo=0,hi=None):
    lo = bisector_left(_list,x,lo,hi)
    _list.insert(lo,x)
