for i in range (int(input())):
    n,a,b=map(int,input().split())
    a=list(input())
    dp=[[10000,10000] for i in range(n+1)]
    dp[0][0]=b
    for i in range(n):
        if a[i]=="0":
            dp[i+1][0]=min(dp[i][1]+2*a+b,dp[i][0]+a+b)
            dp[i+1][1]=min(dp[i][1]+a+2*b,dp[i][0]+2*(a+b))
        else:
            dp[i+1][1]=min(dp[i+1][1],dp[i][1]+a+2*b)
    print(dp[n][0])
