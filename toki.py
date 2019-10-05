count=0
n,m,k=map(int,input().split())
p=[int(i) for i in input().split()]
ans,sum_,now=0,0,0
while(now<m):
    r=((p[now]-sum_-1)/k+1)*k+sum_
    print(r)
    while(now<m and p[now]<=r):
        sum_+=1
        now+=1
    ans+=1
print(ans)
