n=int(input())
a=[int(i) for i in input().split()]
count,count_=0,0
for i in a:
    if i%2!=0:
        count+=1
        ans=a.index(i)+1
    else:
        count_+=1
        ans_=a.index(i)+1
print((ans,ans_)[count>count_])
