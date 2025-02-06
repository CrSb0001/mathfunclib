# Some miscellaneous functions that can come in handy for Project Euler problems.

from math import cos,sin,sqrt,exp,ceil,floor,pi,exp
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
