#Day001 - Standard Deviation.py
import sys;s=sys.stdin.readline

def mean(l):
    return sum(l)/len(l)

def Standard_Deviation(l,mean_lis):
    sum_l=0
    for _ in l:
        sum_l+=(_-mean_lis)**2
        
    return (sum_l/len(l))**.5



    

n=int(s())
lis=[*map(int,s().split())]
#print(mean(lis))
print('%.1f'%Standard_Deviation(lis,mean(lis)))
