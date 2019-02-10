#Day 3: Cards of the Same Suit
from fractions import Fraction as f
from itertools import combinations as c
from math import factorial as fac

card=[*'SCHD'*13]
allkinds=[];samelist=[]
for _ in range(52):
    first=card.pop(_)
    for second in card:
        allkinds+=[[first,second]]
        if first==second:
            samelist+=[[first,second]]
    card=[*'SCHD'*13]
print(f(len(samelist),len(allkinds)))

#02
card=[*'SCHD'*13]
allkinds=list(c(card,2));samelist=[]
for _ in allkinds:
    if _[0]==_[1]:
        samelist+=[[_[0],_[1]]]
print(f(len(samelist),len(allkinds)))
