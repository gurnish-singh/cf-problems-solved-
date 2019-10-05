n=int(input())
a=[int(i) for i in input().split()]
g=0
i=0
while(i<n):
    if a[i]>1:
        temp=a[i]
        a[i]=1
        g+=(temp-1)
    if a[i]<-1:
        temp=a[i]
        a[i]=-1
        g+=(-1-temp)
    i+=1
c=a.count(0)
if a.count(-1)%2 and c<1:
    g+=2
print(g+c)

        
        
        
    
