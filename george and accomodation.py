count=0
for i in range (int(input())):
    n,k=map(int,input().split())
    if(k-n>=2):
        count+=1
print(count)
