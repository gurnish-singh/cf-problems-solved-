def check(x,a):
    moves=0
    for i in range (n//2,n):
        if (x-a[i]>0):
            moves+=x-a[i]
        if moves>k:
            return False
    if moves<=k:
        return True
    else:
        return False
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
a=sorted(a)
j=n//2
r=n//2+1
s=1
b=20000000000
while(s!= b):
    mid=(s+b)//2+1
    if (check(mid,a)):
        s=mid
    else:
        b=mid-1
print(s)
