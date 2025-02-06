import typing

def fibonacci(n,m=None):
    '''
    Finds the n-th Fibonacci number using matrix exponentiation by squaring
    
    Also includes the option to compute the modulus of the result.
    By default this is [None]

    :param n: An integer
    :param m: An integer, default if 10**9 + 7, if specified computes F(n) (mod m).

    :returns: F(n) (mod m) if a modulus is specified, else F(n).
    '''
    if type(n)!=int:
        return "Parameter [n] must be an integer."
    if m!=None and type(m)!=int:
        return "Parameter [m] must be an integer if not [None]."
    if (m!=None and m<=1) or n<=0:
        return "Disallowed integer values detected."
    
    if m != None:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = (f1*f1) % m
            f2, f1, f0 = (f2 * f2 + v) % m, ((f2 + f0) * f1) % m, (v + f0 * f0) % m
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1
    else:
        f2, f1, f0 = 1, 1, 0
        for bit in bin(n)[3:]:
            v = f1*f1
            f2, f1, f0 = f2 * f2 + v, (f2 + f0) * f1, v + f0 * f0
            if bit == '1':
                f2, f1, f0 = f2 + f1, f2, f1
    return f1

def fib_till(lim):
    '''
    Returns a list of all fibonacci numbers up until a limit.

    :param lim: An integer, must be greater than 0.

    :returns: A list of all fibonacci numbers up to that limit.
    '''
    if type(lim)!=int:
        return "Parameter [lim] must be an integer."
    if lim<0:
        return "Disallowed integer values detected."
    
    fib_nums=[]
    n=1
    while fibonacci(n)<=lim:
        fib_nums.append(fibonacci(n))
        n+=1
    return fib_nums

def zeckendorf_rep(x):
    '''
    Finds the Zeckendorf Representation of [x], that is, the sum
    of Fibonacci numbers such that it equals [x] and that the sum
    does not include two consecutive fibonacci numbers.

    :param x: An integer.

    :returns: The Zeckendorf Representation of x.
    '''
    if type(x)!=int:
        return "Parameter [x] must be an integer."
    if x<=0:
        return "Disallowed integer values detected."
    
    zeckrep=[]
    fibs=fib_till(x)[::-1]
    num,count=x,0
    while num!=0:
        if num-fibs[count]>=0:
            num-=fibs[count]
            zeckrep.append(fibs[count])
            count+=1
        count+=1
    return zeckrep
