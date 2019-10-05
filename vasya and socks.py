n,m=map(int,input().split())
count=0
m_=m
while n>0:
    count+=1
    n-=1
    if count==m_:
        m_+=m
        n+=1
print(count)
