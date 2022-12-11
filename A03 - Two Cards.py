n,k=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
for _ in p:
    if k-_ in q: print("Yes"); break
else: print("No")