import math
def secmax(list1):
    maxx=max(list1[0],list1[1]) 
    secondmax=min(list1[0],list1[1]) 
    for i in range(2,len(list1)): 
        if list1[i]>maxx: 
            secondmax=maxx
            maxx=list1[i] 
        else: 
            if list1[i]>secondmax: 
                secondmax=list1[i]
    return secondmax
def secmin(list1):
    maxx=min(list1[0],list1[1]) 
    secondmax=max(list1[0],list1[1]) 
    for i in range(2,len(list1)): 
        if list1[i]<maxx: 
            secondmax=maxx
            maxx=list1[i] 
        else: 
            if list1[i]<secondmax: 
                secondmax=list1[i]
    return secondmax    
n,k=map(int,input().split())
a=[int(i) for i in input().split()]
k=k*8
count=0
a=list(set(a))
memory=n*(math.log(len(a),2))
while(memory>k):
    mx=secmax(a)
    mn=secmin(a)
    for i in range (len(a)):
        if a[i] >mx:
            a[i]=mx
            count+=1
        if a[i]<mn:
            a[i]=mn
            count+=1
    a=list(set(a))
    memory=n*(math.log(len(a),2))
print(count)
            
