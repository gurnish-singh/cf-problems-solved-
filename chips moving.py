n=int(input())
a=[int(i) for i in input().split()]
c=0
for i in a:
    if i%2==1:
        c+=1
print(min(c,n-c))
