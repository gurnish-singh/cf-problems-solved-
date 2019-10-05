n=int(input())
a=[0]*n
count=1
for i in range (n):
    a[i]=input()
for i in range (n-1):
    if a[i]!=a[i+1]:
        count+=1
print(count)
