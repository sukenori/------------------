n=int(input())
a=list(map(int,input().split()))
import itertools
for _ in itertools.combinations(a,3):
    if sum(_)==1000: print("Yes"); break
else: print("No")