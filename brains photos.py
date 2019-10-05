n,m=map(int,input().split())
a=[]
c=0
for i in range (n):
    a.append(list(map(str,input().split())))
for i in range (n):
    for j in range (m):
        if 'C' ==a[i][j] or 'M'== a[i][j] or 'Y' == a[i][j]  :
            c=1
if c==1:
    print('#Color')
else:
    print('#Black&White')
