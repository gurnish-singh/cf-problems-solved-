def computegcd(x, y): 
    gcd=0
    while (y):
        x,y=y,x%y
    return x
c=0
a,b,n=map(int,input().split())
while c!=1:
    g=computegcd(a,n)
    n=n-g
    if n==0:
        print('0')
        c=1
        break
    g=computegcd(b,n)
    n=n-g
    if n==0:
        print('1')
        c=1
        break

    
