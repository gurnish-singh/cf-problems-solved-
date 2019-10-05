n,k=map(int,input().split())
a=[input() for i in range(n)]
ans=0
b=[int(i) for i in input().split()]
d={}
##for i in range (n):
##    for j in range (k):
##        if a[i][j] in d:
##            d[a[i][j]]+=1
##        else:
##            d[a[i][j]]=1
##print(d)
for j in range (k):
    for i in range (n):
        if a[i][j] in d:
            d[a[i][j]]+=1
        else:
            d[a[i][j]]=1
    maximum = max(d, key=d.get)  # Just use 'min' instead of 'max' for minimum.
    ans+=b[j]*d[maximum]
    d={}
print(ans)
        
