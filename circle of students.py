def cround(a):
    n=len(a)
    t=0
    for i in range (n-1):
        if a[i]!=n and abs(a[i]-a[i+1])==1:
            continue
        elif a[i]==n and abs(a[i]-a[i+1])==n-1:
            continue
        else:
            t=1
    if t==0:
        return True
    else:
        return False
def cround2(a):
    n=len(a)
    t=0
    for i in range (n-1):
        if a[i]!=1 and abs(a[i]-a[i+1])==1:
            continue
        elif a[i]==1 and abs(a[i]-a[i+1])==n-1:
            continue
        else:
            t=1
    if t==0:
        return True
    else:
        return False
            
for i in range (int(input())):
    n=int(input())
    a=[int(j) for j in input().split()]
    if  cround(a) or  cround2(a):
        print('YES')
    else:
        print('NO')
    
                
            
                
    
    
