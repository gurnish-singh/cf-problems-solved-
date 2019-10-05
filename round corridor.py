from math import gcd
n,m,q=map(int,input().split())
g=gcd(n,m)
t=n/g
s=m/g
for i in range (q):
    a=[int(i) for i in input().split()]
    if a[0]==1:
        g1=a[1]/t
        if a[2]==1:
           g2=a[3]/t
        else:
            g2=a[3]/s
    else:
        g1=a[1]/s
        if a[2]==2:
           g2=a[3]/s
        else:
           g2=a[3]/t
    if g1==g2:print('Yes')
    elif int(g1)==0 or int(g2)==0:
        print(('yes','no')[abs(g1-g2)<=1])
    else:
        m1=min (int(g1),int(g2))
        g1-=m1
        g2-=m1
        if g1==0 or g2==0:
            print('no')
            continue
        print(('yes','no')[max(g1,g2)>1])        
    
    
    
