#Day4 - Binomial Distribution I

from math import factorial as f

def combi(x,n):
    return f(n)/(f(x)*f(n-x))
    
def Binomial_Distribution(x,n,p):
    return combi(x,n)*(p**x)*((1-p)**(n-x))
    
n=6;x=3
b,g=map(float,input().split())
p=b/(b+g)
l=[Binomial_Distribution(x,n,p) for x in range(3,7)]
print('%.3f'%sum(l))
