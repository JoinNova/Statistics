#Day 5: Geometric Distribution I

from math import e
from math import factorial as f

def Poisson_Distribution(ave,act):
    return (ave**act*e**(-ave)) / f(act)


ave = float(input())
act = int(input())

print('%.3f'%Poisson_Distribution(ave,act))
