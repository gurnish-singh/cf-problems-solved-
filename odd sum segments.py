n=int(input())
for i in range (n):
    m,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    c=0
    for i in (a):
        if i%2==1:
            c+=1
    if c<k or c%2!=k%2:
        print('NO')
        continue
    else:
        print('YES')
        i=0
        while(k!=1):
            if a[i]%2==1:
                    print(i+1,end=' ')
                    k=k-1
            i+=1
        print(m)
            
                
