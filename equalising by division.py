n,k=map(int,input().split())
a=[int(g) for g in input().split()]
ans=10000000
temp=0
for i in range(n):
    c=[19]*n
    temp=0
    for j in range(n):
        cnt=19
        if a[j]==a[i]:
            cnt=0
        elif a[j]<a[i]:
            continue
        else:
            b=a[j]
            d=a[i]
            if b/2>=d:
                cnt=0
                while(b/2>=d):
                    b=b/2
                    cnt+=1
                if int(b)!=d:
                    cnt=19
        c[j]=cnt
    c=sorted(c)
    for p in range (k):
        temp+=c[p]
    if temp<ans:
        ans=temp
print(ans)
        
            
            
            
            
