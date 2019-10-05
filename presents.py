n=int(input())
a=[i for i in input().split()]
for i in range (n):
    print(((a.index(str(i+1))+1)))
