n=int(input())
s=[0]*10
a=list(input())
l,r=0,0
for i in a:
    if i=="L":
        for j in range (10):
            if s[j]==0:
                s[j]=1
                break
    elif i=="R":
        for j in range (1,11):
            if s[-j]==0:
                s[-j]=1
                break
    else:
        s[int(i)]=0
for i in (s):
    print(i,end='')
        
