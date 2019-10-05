n,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[0]*(n-1)
ans=0
for i in range (n-1):
    b[i]=a[i]-a[i+1]
b=sorted(b)
for i in range(k-1):
    ans+=b[i]
ans+=a[n-1]-a[0]
print(ans)
