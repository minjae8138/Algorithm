n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lst = sorted(arr,key = lambda x : x[2])
lst.insert(0,[0,0,0])
dp = [0] * (n+1)
dp[1] = lst[1][1]
res = 0
for i in range(1,len(lst)) :
    max = 0
    for j in range(i-1,0,-1) :
        if lst[i][0] > lst[j][0] and dp[j] >= max :
            max = dp[j]
    dp[i] = lst[i][1] + max
    if dp[i] > res :
        res = dp[i]
print(res)