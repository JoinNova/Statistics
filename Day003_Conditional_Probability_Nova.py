#Day 3: Conditional Probability
from fractions import Fraction as f
children=[['b','b'],['b','w'],['g','b'],['g','g']]
boy=[];onlyboy=[]
for _ in children:
    if _.count('b')>=1:
        boy+=[_]
for _ in boy:
    if _.count('b')==2:
        onlyboy+=[_]
print(f(len(onlyboy),len(boy)))
