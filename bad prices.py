
for j in range (int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    temp=0
    minn=max(a)
    for i in range (n-1,-1,-1):
        if a[i]>minn:
            temp+=1
        minn=min(minn,a[i])
    print(temp)
