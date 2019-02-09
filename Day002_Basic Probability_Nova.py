#Day 2: Basic Probability
from fractions import Fraction as f
dice=[1,2,3,4,5,6];sum_l=[]
for i in range(6):
    for j in range(6):
        if dice[i]+dice[j]<10:
            sum_l.append(dice[i]+dice[j])
print(f(len(sum_l),6*6))

#by rudiejd
from itertools import combinations
from fractions import Fraction as f #modified by nova
dies = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
comb = list(set(combinations(dies, 2)))
res = 0 
for z in comb:
    if z[0] + z[1] <= 9:
        res += 1
print(f(res,len(comb))) #modified by nova

#by rudiejd
from itertools import product
from fractions import Fraction

favorable = sum(1 for x in product(range(1, 7), range(1, 7))
        if sum(x) < 10)

print(Fraction(favorable/36).limit_denominator())
