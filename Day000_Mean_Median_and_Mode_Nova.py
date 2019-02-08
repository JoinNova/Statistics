import sys;s=sys.stdin.readline
import statistics
from collections import*
n=int(s())
l=list(map(int,s().split()))
print('%.1f'%(sum(l)/n))

l.sort()
print('%.1f'%statistics.median(l))

mode=Counter(l)
print(mode.most_common(1)[0][0])
