#Day 1: Interquartile Range

def median(lis):
    n=len(lis)
    if n%2>0:
        idx=n//2
        med=lis[idx]
        lower=lis[:idx]
        upper=lis[idx+1:]
        #print(med,'\n',lis,'\n',lower,upper)
        if med==int(med):med=int(med)
        return med,lower,upper
    else:
        idx=n//2
        med=(lis[idx-1]+lis[idx])/2
        lower=lis[:idx]
        upper=lis[idx:]
        #print(med,'\n',lis,'\n',lower,upper)
        if med==int(med):med=int(med)
        return med,lower,upper
    
import sys;s=sys.stdin.readline
n=int(s())
l=[*map(int,s().split())]
f=[*map(int,s().split())]
fl=[];i=0
for _ in l:
    fl+=[_]*f[i]
    i+=1
fl.sort()
#print(type(median(fl)))
li=median(fl)
low=median(li[1])[0]
up=median(li[2])[0]
print('%.1f'%(up-low))
