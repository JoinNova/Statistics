n = int(input())
x = [*map(int, input().split())]
w = [*map(int, input().split())]
sum_x = sum([a*b for a,b in zip(x,w)])
print(round((sum_x/sum(w)),1))
