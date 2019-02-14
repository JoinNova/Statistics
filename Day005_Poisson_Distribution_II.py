#Day 5: Poisson Distribution II
from math import e
from math import factorial as f

def combi(x,n):
    return f(n)/(f(x)*f(n-x))

def Poisson_Distribution(ave,act):
    return (ave**act*e**(-ave)) / f(act)


ave1,ave2 = map(float,input().split())


print('%.3f'%(160 + 40*(ave1 + ave1**2)))
print('%.3f'%(128 + 40*(ave2 + ave2**2)))
