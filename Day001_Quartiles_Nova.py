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

n=int(input())
lis=[*map(int,input().split())]
lis.sort()
q1=median(median(lis)[1])[0]
q2=median(lis)[0]
q3=median(median(lis)[2])[0]
print(q1,q2,q3,sep='\n')
