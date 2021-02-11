n = int(input())
arr = list(map(int,input().split()))
m = int(input())

dp = [100] * (m+1)
for i in range(len(arr)) :
    for j in range(arr[i],m+1) :
        dp[arr[i]] = 1
        dp[j] = min(dp[j],dp[j-arr[i]]+1)
# print(dp)
print(dp[m])