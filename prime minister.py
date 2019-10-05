n=int(input())
a=[int(i) for i in input().split()]
b=[1]
c=0
i=1
g=a[0]
def check(a):
    g=a[0]
    for i in range (1,n):
        if a[i]*2<=g:
            return True
            break
    else:
        return False
if g>sum(a[1:]):
    print('1','1')
elif check(a):
    while(c==0 and i<n):
            if a[i]*2<=g:
                a[0]+=a[i]
                a[i]=0
                b.append(i+1)
            i+=1
    if a[0]>sum(a[1:]):
        print(len(b))
        for i in (b):
            print(i,end=' ')
    else:
        print('0')

else:
        print('0')
