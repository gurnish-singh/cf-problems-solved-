n=int(input())
m=10**5
for i in range (n):
    p=int(input())
    mnx=-m
    mny=-m
    mxx=m
    mxy=m
    for i in range (p):
       x,y,f1,f2,f3,f4=map(int,input().split())
       if (f1==0):
           mnx=max(mnx,x)
       if (f2==0):
           mxy = min(mxy, y)
       if (f3==0):
           mxx = min(mxx, x)
       if (f4==0):
           mny = max(mny, y)
    if (mnx<=mxx and mny<=mxy):
        print(1,mnx,mny)
    else:
        print(0)
