n=int(input())
sett,count,i=0,0,0
a=[int(i) for i in input().split()]
temp= -1
for i in a:
    if (i)>= temp:
        count+=1
        sett=max(count,sett)
    else:
        count=1
    
    temp=i
print(sett)
        
