from .primes import prime_factors, spf_sieve

def divisors(n, proper = False):
    '''
    Finds all divisors of `n`. If [proper] is True,
    we do not include `n` in the output array.
    '''
    if type(n) != int:
        return "Parameter [n] must be an integer."
    if proper not in [True, False]:
        return f"Parameter [proper] must be one of True or False, got {proper} instead."
    
    pf = prime_factor(n)
    primes = [x for x in pf]
    l = len(primes)
    
    def gen(n = 0):
        if n == l:
            return [1]
        else:
            pows = [1]
            p = primes[n]
            for _ in range(pf[p]):
                pows.append(pows[-1] * p)
            
            div = []
            for q in gen(n + 1):
                for p in pows:
                    div.append(q * p)
            return div
    div = gen()
    if proper:
        div.pop(-1)
        return div
    return div

def sigma(x, n):
    '''
    Implementation of the divisor function sigma(x,n).
    '''
    if type(x) != int or type(n) != int:
        return "Both parameters must be integers."
    
    pf = prime_factors(n)
    total = 1
    if x == 0:
        for p in pf:
            e = pf[p]
            total *= e+1
    else:
        for p in pf:
            e = pf[p]
            total *= ((pow(p, x * (e + 1)) - 1) // (pow(p, x) - 1))
    return total

def div_sieve(x, N):
    '''
    Implementation of the divisior function sigma(x,n) sieve.
    It returns an array such that arr[x]=sigma(x,n).
    '''
    if type(x) != int or type(N) != int:
        return "Both parameters must be integers."
    
    spf = spf_sieve(N)
    d = spf
    for i in range(2, N + 1):
        if spf[i] == i:
            if x == 0:
                d[i] = 2
            else:
                d[i] = 1 + pow(i, x)
        else:
            p = spf[i]
            t = i // p
            e = 1
            while t % p == 0:
                e += 1
                t //= p
            if x == 0:
                d[i] = d[t] * (e + 1)
            else:
                d[i] = d[t] * ((pow(p, x * (e + 1)) - 1) // (pow(p, x) - 1))
    return d
