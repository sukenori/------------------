h,w=map(int,input().split())
cx=[[0]*(w+1) for i in range(h+1)]
for i in range(h):
    cwx=0
    for j,_ in enumerate(map(int,input().split())):
        cwx+=_
        cx[i+1][j+1]=cx[i][j+1]+cwx
q=int(input())
for i in range(q):
    a,b,c,d=map(int,input().split())
    print(cx[c][d]-cx[a-1][d]-cx[c][b-1]+cx[a-1][b-1])