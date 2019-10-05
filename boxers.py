n=int(input())
a=[int(i) for i in input().split()]
a.sort()
a.reverse()
lst =a[0]+2
ans=0
for i in a:
    cur=-1
    for j in range (1,-2,-1):
        if i+j>0 and i+j<lst:
            cur=i+j
            break
    if cur==-1:
        continue
    ans+=1
    lst=cur
print(ans)
    
