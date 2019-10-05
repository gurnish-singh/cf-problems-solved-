a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
n=b[a[1]-1]
count=0
for i in range (a[0]):
    if n<=b[i] and  b[i]!=0:
        count+=1
print (count)
