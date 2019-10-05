n=int(input())
for i in range (n):
    a=[int(i) for i in input().split()]
    ans=sum(a)//2
    print(ans)
