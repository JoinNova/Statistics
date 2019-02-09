#Day 2: Compound Event Probability
from fractions import Fraction as f
x=['r','r','r','r','b','b','b']
y=['r','r','r','r','r','b','b','b','b']
z=['r','r','r','r','b','b','b','b']
group=[x,y,z]
black_list=[]
red_list=[]
result=0
Probability=0
for _ in group:
    black=0
    for ball in _:
        if ball=='b':
            black+=1
    black_list+=[[black,len(_)]]
#print(black_list)
for bl in black_list:
    result=f(bl[0],bl[1])
    for re in black_list:
        if bl!=re:
            result*=(1-f(re[0],re[1]))
    Probability+=result
print(f(Probability))
            
