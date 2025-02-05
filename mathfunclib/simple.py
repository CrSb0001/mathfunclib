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
            n=list(str(n))
            for i in range(len(n)):
                n[i]=int(n[i])
            return n
    
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
