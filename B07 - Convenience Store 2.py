t,n=[int(input()) for i in range(2)]
fg=[0]*(t+1)
for i in range(n):
    l,r=map(int,input().split())
    fg[l]+=1; fg[r]-=1
g=[0]
for _ in fg: g+=[g[-1]+_]
for _ in g[1:t+1]: print(_)