t='RGB'
for i in range (int(input())):
    n,k=map(int,input().split())
    a=str(input())
    ans=10**9
    for j in range (0,n-k+1):
        for off in range (0,3):#offeset
            cur=0
            for p in range (0,k):
                if (a[j+p]!=t[(p+off)%3]):
                    cur+=1
            ans=min(ans,cur)
    print(ans)            
                
                
                
