n,x,y=map(int,input().split())
a=[int(i) for i in input().split()]
for d in range (n):# d is our day
    # our expression should be d-x<= j <d
    j=d-1# j should be lesse than d
    f1,f2=0,0
    while(j>=d-x):
        if j<0:break
        if (a[d]>=a[j]):
            f1=1
            break
        j-=1#we have to consider it for all j in the range
    # now we need to check the second condition d<j<=d+y
    j=d+1
    while j<=d+y:
        if j>n-1:break
        if a[d]>=a[j]:
            f2=1
            break
        j+=1
    if (f1==0 and f2==0):print(d+1);break
        
    
