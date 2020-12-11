## DP

## Bottom-up(점화식)
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1) :
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

## Top-down(메모제이션)
# n = int(input())
# dp = [0] * (n+1)
# def dfs(n) :
#     if n==1 or n==2 :
#         return n
#     if dp[n] > 0 :
#         return dp[n]
#     else :
#         dp[n] = dfs(n-1) + dfs(n-2)
#         return dp[n]
# print(dfs(n))
