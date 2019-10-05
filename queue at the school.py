n,t=map(int,input().split())
a=(input())
for j in range (t):
    if ('BG' in a):
        i=0
        while i <=(n-2):
            if (a[i]=='B' and a[i+1]=='G'):
                t = list(a)
                temp=t[i]
                t[i]=t[i+1]
                t[i+1]=temp
                a=''.join(t)
                i+=2
            else:
                i+=1
print(a)
                
            
