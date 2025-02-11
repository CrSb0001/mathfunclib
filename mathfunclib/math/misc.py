# Some miscellaneous functions that can come in handy for Project Euler problems.

from math import cos,sin,sqrt,exp,ceil,floor,pi,gcd
from decimal import *

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
