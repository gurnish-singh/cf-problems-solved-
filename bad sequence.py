n=int(input())
a=list(input())
c=0
for i in a:
    if i=='(':
        c+=1
    else:
        c-=1
    if c<=-2:
        break
if (c<=-2 or c!=0):
    print('NO')
else:
    print("Yes")
    
