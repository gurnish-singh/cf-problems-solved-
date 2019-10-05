n,k=map(int,input().split())
a=dict()
ans =0
count=0
for i in range (n):
    b=int(input())
    if b in a :
        a[b]+=1
    else:
        a[b]=1
for key in a:
    if a[key]%2==0:
        ans+=a[key]
        a[key]=0
    else:
        ans+=(a[key]-1)
        a[key]=1
for key in a:
    if a[key]==1:
        count+=1
if count%2==0:
    ans+=count//2
else:
    ans+=(count//2)+1
print(ans)

