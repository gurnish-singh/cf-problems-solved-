n=int(input())
for i in range (n):
    n,m=map(int,input().split())
    temp,temp1,temp2=0,0,0
    k=n//m # the number of integers from 1 to n divisible by m
    temp=k//10
    for i in range (9):
        temp1+=m*(i+1)%10# the sum of all the last digits for i*m
    for i in range (k%10):
        temp2+=m*(i+1)%10
    print(temp*temp1 +temp2)
