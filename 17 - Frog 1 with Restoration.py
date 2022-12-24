n=int(input())
h=list(map(int,input().split()))
dp=[0,abs(h[1]-h[0])]
for i in range(2,n):
    dp.append(min(dp[i-2]+abs(h[i-2]-h[i]),dp[i-1]+abs(h[i-1]-h[i])))
