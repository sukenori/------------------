n,k=map(int,input().split())
a=list(map(int,input().split()))
r=1; sr=0
for i in range(n):
    sr+=r-i-1
    while True:
        if a[r]-a[i]<=k:
            r+=1; sr+=1
            if r==n: break
        else: break
print(sr)