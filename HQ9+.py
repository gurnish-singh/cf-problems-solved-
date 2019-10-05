a=input()
i=0
count=0
for i in range (len(a)):
    if(a[i] in 'HQ9'):
        count=1
print(('NO','YES')[count==1])
