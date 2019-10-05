an=int(input())
a=[int(i) for i in input().split()]
bn=int(input())
b=[int(i) for i in input().split()]
t=0
for i in a:
    for j in b:
        if t==1 :break
        if (i+j) not in a and (i+j) not in b:
            print(i,j)
            t=1
            break
        
