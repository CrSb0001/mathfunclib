# Some miscellaneous functions that can come in handy for Project Euler problems.

from math import cos,sin,sqrt,exp,ceil,floor,pi,gcd
from decimal import *
from .primes import is_prime

def compute_sin(N):
    m,i=10**8,None
    getcontext().prec=50
    _pi=Decimal('3.1415926535897932384626433832795028841971693993751')
    
    for n in range(N+1):
        if round(n**0.5)**2!=n:
            x=_pi*Decimal(n).sqrt()
            v=(Decimal(x).exp()-Decimal(-x).exp())/Decimal(2)
            z=sin(pi*sqrt(n))
            
            t1=min(ceil(v)-v,v-floor(v))
            t2=min(ceil(z)-z,z-floor(z))
            if t1<m:
                m,i=t1,-n
            if t2<m:
                m,i=t2,n
    return i

def compute_cos(N):
    m,i=10**8,None
    getcontext().prec=50
    _pi=Decimal('3.1415926535897932384626433832795028841971693993751')
    for n in range(N+1):
        if round(n**0.5)**2!=n:
            x=_pi*Decimal(n).sqrt()
            v=(Decimal(x).exp()+Decimal(-x).exp())/Decimal(2)
            z=cos(pi*sqrt(n))
            
            t1=min(ceil(v)-v,v-floor(v))
            t2=min(ceil(z)-z,z-floor(z))
            if t1<m:
                m,i=t1,-n
            if t2<m:
                m,i=t2,n
    return i

def sum_multiples_under_lim(m,n,lim):
    if type(m)!=int or type(n)!=int:
        return "All parameters must be integers."
    if lim!=float('inf') and type(lim)!=int:
        return "Parameter [lim] must be integer if not float('inf')"
    if lim<=0:
        return "Parameter [lim] must be greater than 0."
    
    def res(u,v,d=0):
        if d!=float('inf'):
            q=(v-1)//u
            return u*q*(q-1)//2
        else: # THIS part is helpful for the bonus Project Euler -1.
            q=(u+v-u*v)//gcd(u+v-u*v,12)
            r=12//gcd(u+v-u*v,12)
            if r==1:
                return f'{q}'
            else:
                return f'{q}/{r}'
    return res(m,lim)+res(n,lim)-res(n*m,lim) if lim!=float('inf') else res(n,m,lim)

def last_nzero_digit_n_fac(n):
    '''
    Computes the last nonzero digit of n! = n*(n-1)*(n-2)*(n-3)*...*3*2*1,
    where 0! == 1! == 1.
    
    Usually, we can only compute the last nonzero digit of up to around (10**697)!
    due to recursion limitations, but we can add the following setup beforehand
    to compute up to the last nonzero digit of (10**40000)! correctly before we
    start to run into issues with time limits:
    ```
    import resource,sys
    from functools import lru_cache
    resource.setrlimit(resource.RLIMIT_STACK,(2**29,-1))
    sys.setrecursionlimit(10**9)
    
    @lru_cache
    # our function here
    ```
    '''
    return int('1126422428'[n]) if 0<=n<10 else int('2486'[(n//5-1)%4])*last_nzero_digit_n_fac(n//5)*last_nzero_digit_n_fac(n%5)%10

def sqrt_dec_expn_sum(n,d):
    '''
    This function gives the sum of the first `d` digits
    of the decimal expansion of the fractional part of sqrt(n)
    
    Helpful for Project Euler's bonus problem root(13).
    '''
    if type(n)!=int or type(d)!=int:
        return "Both parameters must be integers."
    if round(n**0.5)**2==x:
        return "Do it yourself!" # Hint: It's 0.
    if n<0:
        return "Cannot give a complex result."
    if d<=0:
        return "Parameter [d] must be greater than 0."
    
    getcontext().prec = d+5
    v = str(Decimal(n).sqrt())[3:p+3]
    return sum(int(x) for x in v)

def is_stealthy(n):
    '''
    AKA bipronic numbers (OEIS A072389), this function finds numbers
    of the form x*(x+1)*y*(y+1) for nonnegative x,y. We initialize the
    sequence with 0 == 0*(0+1)*1*(1+1).
    '''
    if type(n)!=int:
        return "Parameter [n] must be an integer."
    
    if n==0:
        return True
    if n<0:
        return False
    elif is_prime(n):
        return False
    for i in range(1,n//2+2):
        for j in range(1,i+1):
            if i*(i+1)*j*(j+1):
                return True
    return False

def can_win_nim_gen(n,k):
    '''
    Problem statement:
    > You are playing Nim with your friend with the rules as follows:
    > 1. Initially, there is an arbitrary number of stones on the table.
    > 2. You and your friend will alternate taking turns; you go first.
    > 3. On each turn, the person whose turn it is will remove 1 to `n`
         stones from the pile.
    > 4. The one who removes the last stone is the winner.
    
    Goal: Given `k` stones, return True if you can win the game assuming
          perfect play, else return False.
    '''
    if type(n)!=int or type(k)!=int:
        return "Both parameters must be integers."
    
    return True if (n%(k+1)!=0 or n==0) else False
