'''
from math import exp, pi, erf, sqrt

mean, dev = map(float,input().split())
#lim = float(input())
#low,hi = map(int,input().split())

def Normal_DistributionI(mu, sigma):
    def gauss_cdf(x):
        nonlocal mu, sigma
        arg = (x-mu)/(sigma*sqrt(2))
        return (erf(arg) + 1) / 2
    return gauss_cdf

#gauss_cdf = Normal_DistributionI(mean, dev)
#ans1 = gauss_cdf(hi)
#ans2 = gauss_cdf(hi)-gauss_cdf(low)

print("%.2f" %ans1)
print("%.2f" %ans2)
print("%.2f" %ans3)
'''

from math import sqrt,erf

def Normal_DistributionII(arg, mu, sigma):
    param = (arg-mu)/(sigma*sqrt(2))
    return ( 1 + erf(param) ) * 0.5

mean, dev = [float(num) for num in input().split()]
hi=float(input())
low=float(input())


ans1 = 100 * (1 - Normal_DistributionII(hi, mean, dev))
ans2 = 100 * (1 - Normal_DistributionII(low, mean, dev))
ans3 = 100 * Normal_DistributionII(low, mean, dev)

print("%.2f" %ans1)
print("%.2f" %ans2)
print("%.2f" %ans3)
