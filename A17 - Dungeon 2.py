n=int(input())
a=[0]+list(map(int,input().split()))
b=[0,0]+list(map(int,input().split()))
dp=[0,a[1]]
for i in range(2,n):
    dp.append(min(dp[i-2]+b[i],dp[i-1]+a[i]))
d=[n]; i=n-1
while True:
    if i==1:
        d.append(1)
        i=i-1
    if i==0:
        break
    if dp[i-2]+b[i]<=dp[i-1]+a[i]:
        d.append(i-1)
        i=i-2
    else:
        d.append(i)
        i=i-1
print(len(d))
print(*sorted(d))