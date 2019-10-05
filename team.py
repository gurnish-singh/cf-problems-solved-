count=0
for i in [0]*int(input()):
    a=[(j) for j in input().split()]
    count_= 0
    for k in range (3):
        if a[k]== '1':
            count_+=1
    if count_>=2:
        count+=1
    count_=0
print (count)

