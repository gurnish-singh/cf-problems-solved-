k,n,w=map(int,input().split())
cost=k*w*(w+1)/2
print((int(cost-n),'0')[n>cost])





