g=int(input())
for i in range (g):
    n,m,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    i=0
    count=0
    c=0
    while(i<n-1):
            temp=a[i]
            temp1=max(0,a[i+1]-k)
            if a[i]>temp1:
                m+=(temp-temp1)
            else:
                m-=abs(temp1-temp)
            i+=1
            if m<0:
                c=1
                break
    print(("YES","NO")[c==1])

            
            
           
            
