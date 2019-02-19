from math import exp, pi, erf, sqrt

def Normal_DistributionI(mu, sigma):
    def gauss_cdf(x):
        nonlocal mu, sigma
        arg = (x-mu)/(sigma*sqrt(2))
        return (erf(arg) + 1) / 2
    return gauss_cdf

def Normal_DistributionII(arg, mu, sigma):
    param = (arg-mu)/(std*sqrt(2))
    return ( 1 + erf(param) ) * 0.5

def less_than_boundary_cdf(limit, amount, mean, dev):
    return 0.5*(1+erf((limit-amount*mean)/(sqrt(amount)*dev*sqrt(2))))

limit = int(input())
amount = int(input())
mean = int(input())
dev = int(input())

result=less_than_boundary_cdf(limit, amount, mean, dev)

print('%.4f'%result)
