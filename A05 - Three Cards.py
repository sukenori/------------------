n,k=map(int,input().split())
s=[]
for i in range(1,n+1):
    for j in range(1,n+1):
        for l in range(1,n+1):
            s.append(i+j+l)
print(s.count(k))