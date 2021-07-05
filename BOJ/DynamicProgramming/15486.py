n = int(input())
time = []
money = []
dp = [0]*(n+1)
for i in range(n) :
    a,b = map(int,input().split())
    time.append(a)
    money.append(b)

large = 0
for i in range(n) :
    large = max(large,dp[i])
    if i+time[i] > n :
        continue
    dp[i+time[i]] = max(large+money[i],dp[i+time[i]])
print(max(dp))




