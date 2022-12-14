h,w,n=map(int,input().split())
import numpy as np
hw=np.zeros((h,w+2))
for i in range(n):
    a,b,c,d=map(int,input().split())
    hw[a-1:c,b]+=1
    hw[a-1:c,d+1]-=1
chw=[[0]*(w+1) for i in range(h)]
for i in range(h):
    for j in range(1,w+1):
        chw[i][j]=chw[i][j-1]+int(hw[i,j])
for _ in chw:
    print(*_[1:])