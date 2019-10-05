
for i in range (int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a=sorted(a)
    area=a[0]*a[-1]
    t=0
    for i in range (n):
        lf=i*2
        rg=4*n-(i*2)-1
        if a[lf]!=a[lf+1]or a[rg]!=a[rg-1] or a[lf]*a[rg]!=area:
            t=1
    print(("YES","NO")[t==1])
        
    
    
