import typing
from math import sqrt,gcd,floor
from .simple import extended_euclid_alg

def continued_frac_sqrt(x, limit=100):
    '''
    Returns the continued fraction for the
    square root of our input, x.
    
    :param x: an integer
    :param limit: (optional) The max amount of terms in the expansion
    
    :returns: A list containg the cont. frac. expansion of sqrt(x)
    
    Stops automatically if we reach {limit} number of terms (default: 100)
    '''
    if type(x) != int or type(limit) != int:
        return "All values must be integers"
    
    m0,d0,a0 = 0,1,floor(sqrt(x))
    temp_list = [a0]
    
    while True:
        mn = int(d0*a0-m0)
        dn = int((x-mn**2)/d0)
        an = int(floor((sqrt(x)+mn)/dn))
        temp_list.append(an)
        if an == 2*floor(sqrt(x)):
            break
        if len(temp_list) == limit:
            break
        m0,d0,a0=mn,dn,an
    return temp_list

def overall_frac(cf):
    '''
    :param cf: Continued fraction of a number

    :returns numerator: An integer that represents the numerator of the fraction
    :returns denominator: An integer that represent the denominator of the fraction.
    '''
    if type(cf)!=list:
        return "Parameter [cf] must be a list."
    if len(cf)==0:
        return "Parameter [cf] must have items in its list"
    for i in range(len(cf)):
        if type(cf[i])!=int:
            return "Paramter [cf] must only contain integers."
    
    cf=cf[::-1]
    denominator=1
    numerator=cf[0]
    for x in range(1,len(cf)):
        numerator,denominator=cf[x]*numerator+denominator,numerator
    return numerator,denominator

def phi(n):
    '''
    Implementation of Euler's Toitent function, which counts the number
    of positive integers up to a given [n] that are relatively prime
    to [n].

    :param n: An integer

    :returns: The number of positive integers up to [n] that are
              relatively prime to [n]
    '''
    if type(n)!=int or n<0:
        return "Parameter [n] must be a positive integer."
    
    if n==1 or n==0:
        return n
    phi_int,d=1,2
    while n>1:
        count=0
        while n%d==0:
            count+=1
            n//=d
        if count>0:
            phi_int*=(pow(d,count-1))*(d-1)
        d+=1
        if d*d>n:
            if n>1:
                phi_int*=int(n-1)
            break
    return phi_int

def phi_sieve(n):
    '''
    A sieve for Euler's Toitent Function

    :param n: An integer

    :returns: An array where arr[x]==phi(x)
    '''
    if type(n)!=int or n<0:
        return 'Parameter [n] must be a positive integer.'
    
    phi_arr = [i for i in range(n+1)]
    for p in range(2,n+1):
        if phi_arr[p]==p:
            phi_arr[p]-=1
            for i in range(2*p,n+1,p):
                phi_arr[i]-=(phi_arr[i]//p)
    return phi_arr

def pythagorean_triples(lim,non_prim=False):
    '''
    Generates all Pythagorean triplets up to [limit].

    :param lim: Integer, limit for up to which Pythagorean Triples can be generated.
    :param non_prim: Optional bool, generates all triples if set to [True], else only generates
                     primitive triplets. Set to [False] by default.

    :returns: A list containing all desired triplets.
    '''
    if type(lim)!=int:
        return "Paramter [lim] must be an integer."
    if non_prim!=False and non_prim!=True:
        return "Paramter [non_prim] must be one of [True] or [False]"
    
    triples=[]
    for m in range(2,int(sqrt(lim))+1):
        for n in range(1+(m%2),m,2):
            if gcd(m,n)==1:
                a=m**2+n**2
                b=m**2-n**2
                c=m*n*2
                if a<limit:
                    if non_prim:
                        for k in range(1,int(lim/a)+1):
                            triples.append([k*b,k*c,k*a])
                    else:
                        triples.append([b,c,a])
    return triples

def CRT(a1,a2,n1,n2):
    '''
    Simple implementation of the Chinese Remainder Theorem.

    :param a1: Integer
    :param a2: Integer
    :param n1: Integer
    :param n2: Integer

    :returns: The unique solution to x == a1 mod n1, x == a2 mod n2.
    '''
    if type(a1)!=int or type(a2)!=int or type(n1)!=int or type(n2)!=int:
        return "All parameters must be integers."
    if a1>=n1 or a2>=n2:
        return "Wrong values were inputted."
    if n1==0 or n1==1 or n2==0 or n2==1:
        return "Wrong values were inputted."
    
    p,q=pow(n1,-1,n2),pow(n2,-1,n1)
    return (a1*q*n2 + a2*p*n1)%(n1*n2)

def generalized_CRT(a1,a2,n1,n2):
    '''
    Implementation of the generalized Chinese Remainder Theorem.

    :param a1: Integer
    :param a2: Integer
    :param n1: Integer
    :param n2: Integer

    :returns: The unique solution to x == a1 mod n1, x == a2 mod n2
    '''
    if type(a1)!=int or type(a2)!=int or type(n1)!=int or type(n2)!=int:
        return "All parameters must be integers."
    
    g,u,v=extended_euclid_alg(n1,n2)
    if g==1:
        return ((a1*v*n2+a2*u*n1)//g)%(n1*n2)
    M=(n1*n2)//g
    if (a1%g)!=(a2%g):
        return "No solution."
    return ((a1*v*n2+a2*u*n1)//g)%M

def partition(x,L,show=True):
    '''
    :param x: The number that we want to find partitions of.
    :param L: List of numbers we can use for partitions.
    :param show: Optional, default is true. If False, it shows
                 how many partitions there are, else it outputs
                 all the partitions.

    :returns: #of partitions or all partitions based on the val
              of [show].
    '''
