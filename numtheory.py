import typing

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
    :param non_prim: Bool, generates all triples if set to [True], else only generates
                     primitive triplets.

    :returns: A list containing all desired triplets.
    '''
