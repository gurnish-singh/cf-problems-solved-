n=int(input())
for i in range (n):
    ans=1000000
    penality =0
    r,c=map(int,input().split())
    a=[input() for j in range (r)]
    row=[0]*r
    col=[0]*c
    for j in range (r):
        for k in range (c):
            if a[j][k]=='.':
                row[j]+=1
                col[k]+=1
    for j in range (r):
        for k in range (c):
            if a[j][k]=='.':
                penalty=1
            else:
                penalty=0
            temp=row[j]+col[k]-penalty
            if temp<ans:
                ans=temp
    print(ans)
        
    
