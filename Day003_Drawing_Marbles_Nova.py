#Day 3: Drawing Marbles
from fractions import Fraction as f
from itertools import combinations as c
from math import factorial as fac

bag=[*['RED']*3,*['BLUE']*4]
firstred=[];secondblue=[]
for _ in range(7):
    first=bag.pop(_)
    if first=='RED':
        for second in bag:
            firstred+=[[first,second]]
            if second=='BLUE':
                secondblue+=[[first,second]]
    bag=[*['RED']*3,*['BLUE']*4]
print(f(len(secondblue),len(firstred)))
