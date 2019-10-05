
k,l,m,n,d=[int(input()) for i in 'klmnd']
g=[0]
g=[0]*(d+1)
if (k ==1 or l==1 or m==1 or n==1):
    print(d)
else:
    for i in range (k,d+1,k):
       g[i]=1
    for i in range (l,d+1,l):
       g[i]=1
    for i in range (m,d+1,m):
       g[i]=1
    for i in range (n,d+1,n):
       g[i]=1
    print(int(sum(g)))
