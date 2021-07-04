# DFS 풀이

n = int(input())
time = []
money = []
for i in range(n) :
    a,b = map(int,input().split())
    time.append(a)
    money.append(b)

large = 0
def dfs(l,m) :
    global large
    if l == n :
        if m > large :
            large = m
            return large
    else :
        if l+time[l] <= n :         # 시간이 n 이하면 시간과 금액에 대해 각각 l만큼 이동
            dfs(l+time[l],m+money[l])
        dfs(l+1,m)                  # 그렇지 않으면 금액변화 없이 한칸씩 이동
dfs(0,0)
print(large)


# DP 풀이

n = int(input())
time = []
money = []
dp = []
for i in range(n) :
    a,b = map(int,input().split())
    time.append(a)
    money.append(b)
    dp.append(b)
dp.append(0)            # i+1과 비교해야해서 0을 하나 추가하는 작업이 필요
for i in range(n-1,-1,-1) :
    if time[i] + i > n :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1],money[i]+dp[i+time[i]])
print(dp[0])





















