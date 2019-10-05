n,k=map(int,input().split())
if n%2!=0:
    if k>(n/2 +1):
        ans=(k-(n//2+1))*2
    else:
        ans=k*2-1
else:
    if k>n/2:
        ans=(k-n/2)*2
    else :
        ans =k*2-1
print(int(ans))

    
