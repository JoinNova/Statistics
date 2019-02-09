#by Day 2: More Dice
from fractions import Fraction as f
dice=[1,2,3,4,5,6];sum_l=[]
for i in range(6):
    for j in range(6):
        if dice[i]!=dice[j] and dice[i]+dice[j]==6:
            sum_l.append(dice[i]+dice[j])
print(f(len(sum_l),6*6))
