n=int(input())
count=0
if n%2==0:
    ans=n/2
else:
    ans=-(n//2+1)
print(int(ans))
