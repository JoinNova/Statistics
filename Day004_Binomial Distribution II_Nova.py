# Enter your code here. Read input from STDIN. Print output to STDOUT
#Day4 - Binomial Distribution II

from math import factorial as f

def combi(x,n):
    return f(n)/(f(x)*f(n-x))
    
def Binomial_Distribution(x,n,p):
    return combi(x,n)*(p**x)*((1-p)**(n-x))
    
p,n=map(int,input().split())
p/=100
la=[Binomial_Distribution(x,n,p) for x in range(3)]
lb=[Binomial_Distribution(x,n,p) for x in range(2,11)]
print('%.3f'%sum(la))
print('%.3f'%sum(lb))
