count=0;maxi=count;
for i in [0]*int(input()):
    a=[int (j) for j in input().split()]
    count-=a[0]
    count+=a[1]
    if count>maxi:maxi=count
print(maxi)
