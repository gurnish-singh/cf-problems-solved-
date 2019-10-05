n=int(input())
for i in range(n):
    p=int(input())
    a=[int(i) for i in input().split()]
    g,p=1,0
    for k in a:
        g=g*k
    for j in a:
        p=p+j
    g=g/p
    ans=max(g%(10**9+7),g)
    print('Case #'+repr(i+1)+':')
    print(int(ans))
    
