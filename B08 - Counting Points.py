cxy=[[0]*1501 for i in range(1501)]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    cxy[x][y]+=1
for i in range(1,1501):
    for j in range(1,1501):
        cxy[i][j]+=cxy[i][j-1]
for i in range(1,1501):
    for j in range(1,1501):
        cxy[i][j]+=cxy[i-1][j]
q=int(input())
for i in range(q):
    a,b,c,d=map(int,input().split())
    print(cxy[c][d]-cxy[c][b-1]-cxy[a-1][d]+cxy[a-1][b-1])