from math import exp, pi, erf, sqrt

mean, dis = map(int,input().split())
lim = float(input())
low,hi = map(int,input().split())


def Normal_Distribution(mu, sigma):
    def gauss_cdf(x):
        nonlocal mu, sigma
        arg = (x-mu)/(sigma*sqrt(2))
        return (erf(arg) + 1) / 2
    return gauss_cdf

gauss_cdf = Normal_Distribution(mean, dis)
ans1 = gauss_cdf(lim)
ans2 = gauss_cdf(hi) - gauss_cdf(low)
print("{:.3f}".format(ans1))
print("{:.3f}".format(ans2))
