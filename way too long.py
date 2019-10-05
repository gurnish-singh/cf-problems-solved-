a=[int(i) for i in input().split()]
print(a)
b=[int(j) for j in input().split()]
count=0
for i in [0]*a[0]:
    if (b[i]>=b[a[1]-1]):
        count+=1
    else:
        count-=1
print (count)
