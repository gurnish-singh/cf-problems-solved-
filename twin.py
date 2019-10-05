input()
a=sorted(map(int,input().split()))
s,count=0,0
while(s<=sum(a)):
    s+=a.pop()
    count+=1
print(count)
