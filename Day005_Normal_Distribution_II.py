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
