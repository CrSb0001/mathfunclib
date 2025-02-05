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
    if type(n)!=int or type(b)!=int:
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
        return [n]
    if b==10:
        return list(str(n))
    digits=[]
