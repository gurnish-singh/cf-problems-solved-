n,m=map(int,input().split())
a=[ int(i) for i in input().split()]
a=sorted(a)
best=1000
for k in range (m-n+1):
    best=min(best,a[k+n-1]-a[k])
print(best)
