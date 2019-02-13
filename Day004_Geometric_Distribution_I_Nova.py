#Day 4: Geometric Distribution I


from math import factorial as f

def combi(x,n):
    return f(n)/(f(x)*f(n-x))
    
def Binomial_Distribution(x,n,p):
    return combi(x,n)*(p**x)*((1-p)**(n-x))

def Geometric_Distribution(n,p):
    return (1-p)**(n-1)*p

a,b=map(int,input().split())
case=int(input())

print('%.3f'%Geometric_Distribution(case,a/b))
