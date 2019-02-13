#Day 4: Geometric Distribution II

from math import factorial as f

def combi(x,n):
    return f(n)/(f(x)*f(n-x))
    
def Binomial_Distribution(x,n,p):
    return combi(x,n)*(p**x)*((1-p)**(n-x))

def Geometric_Distribution(n,p):
    return (1-p)**(n-1)*p


a,b=map(int,input().split())
case=int(input())
p=a/b

print('%.3f'%sum([Geometric_Distribution(x,p) for x in range(1,case+1)]))
