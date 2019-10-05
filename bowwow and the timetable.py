n=input()
n= int(n,2) 
n=n%2**100
i=0
t=0
while (t==0):
    if n>4**i:
        i+=1
    else:
        t=1
print(i)
        
    
