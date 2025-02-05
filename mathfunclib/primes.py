import typing
from math import sqrt

def is_prime(n):
    '''
    A simple is_prime function.
    Returns if the input is prime or not.

    :param n: Integer coefficient.

    :returns: If [n] is prime or not.
    '''
    if type(n)!=int:
        return "Parameter must be an integer."
    
    if x<=1:
        return False
    elif x<=3:
        return True
    elif x%2==0:
        return False
    else:
        for i in range(3,int(sqrt(x))+1,2):
            if x%i==0:
                return False
        return True

def prime_sieve(lim,val=True):
    '''
    A prime sieve.

    :param lim: The limit to do the sieve until.
    :param val: Optional, if set to False will only outupt whether or not
                the index if prime.

    :returns: A list of prime values.
    '''
    if type(lim)!=int:
        return "Parameter [lim] must be an integer."
    if val!=True and val!=False:
        return "Parameter [val] must be one of [True] or [False]."

    p_list=[]
    if val:
        for i in range(2,limit+1):
            if isprime(i):
                p_list.append(i)
        return p_list
    else:
        for i in range(limit+1):
            if isprime(i):
                p_list.append(True)
            else:
                p_list.append(False)
        return p_list

def prime_factors(n):
    '''
    A dictionary containing the prime factors of [n].

    :param n: Integer.

    :returns: Hashmap containing the prime factors of [n].
    '''
    if type(n)!=int:
        return "Parameter [n] must be an integer."
    
    factors={}
    d=2
    while n>1:
        while n%d==0:
            if d in factors:
                factors[d]+=1
            else:
                factors[d]=1
            n//=d
        d+=1
        if d*d>n:
            if n>1:
                if d in factors:
                    factors[n]+=1
                else:
                    factors[n]=1
            break
    return factors

def sum_of_primes(n):
    '''
    Fast sum of primes function.

    :param n: Integer, we sum all primes up until [n].

    :returns: The sum of primes up until [n].
    '''
    if type(n) != int:
        return "n must be an integer"
    
    r = int(n ** 0.5)
    assert r * r <= n and (r + 1) ** 2 > n
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i: i * (i + 1) // 2 - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:
            sp = S[p - 1]
            p2 = p * p
            for v in V:
                if v < p2: break
                S[v] -= p * (S[v // p] - sp)
    return S[n]

def fermat_primality_test(n,tests=2):
    '''
    Uses Fermat's Primality Test to determine if a number is prime.

    :param n: Integer to test if is prime.
    :param tests: Number of tests to use. Default is 2.

    :returns: If the number is prime or not according to the tests.
    
    If n<10**5 then we just use is_prime as it isn't too inefficient
    for small integers.
    '''
    if type(n)!=int or type(tests)!=int:
        return "All parameters must be integers."
    if n<=1:
        return "Invalid value."
    if tests<=1:
        return "Invalid number of tests."
    
    if n<10**5:
        return is_prime(n)
    else:
        for x in range(tests):
            if pow(2*(x+2),n-1,n)!=1:
                return False
        return True
