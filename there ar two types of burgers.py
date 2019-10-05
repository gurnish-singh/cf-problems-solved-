for i in range (int(input())):
    b,p,f=map(int,input().split())
    h,c=map(int,input().split())
    ans=0
    temp=0
    gg=0
    if h>c:
        p,f=f,p
    for i in range (1,f+1):
        if b>=2*i and b>1:
            ans=i*c
            temp=i
    b=b-2*temp
    for j in range(1,p+1):
        if b<=1:
            break
        if b>=2*j and b>1:
            gg=j*h
    ans+=gg
    print(ans)
        
        
        
        
