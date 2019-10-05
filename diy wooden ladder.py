n=int(input())
for i in range (n):
    p=int(input())
    a=[int(i) for i in input().split()]
    max_=max(a[0],a[1]) 
    secondmax=min(a[0],a[1]) 
    for i in range(2,len(a)): 
        if a[i]>max_: 
            secondmax=max_
            max_=a[i] 
        else: 
            if a[i]>secondmax: 
                secondmax=a[i]
    ans=min(secondmax-1,p-2)
    print(ans)

            
        

