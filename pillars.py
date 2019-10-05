n=int(input())
a=[int(i) for i in input().split()]
c=a.index(max(a))
count=0
for i in range (1,c+1):
    if a[i]>a[i-1]:
        continue
    else:
        count=1
        break
if count==0:
    for i in  range (c,n-1):
        if a[i]>a[i+1]:
            continue
        else:
            count=1
print(('YES','NO')[count==1])
    
        
    

