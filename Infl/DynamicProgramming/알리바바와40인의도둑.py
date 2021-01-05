n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

# bottom-up 풀이

# 맨윗줄과 맨아랫줄(0행과 0열) 값 변환
for i in range(1,n) :
    arr[i][0] += arr[i-1][0]
    arr[0][i] += arr[0][i-1]

# 나머지 칸 값 변환, 위의칸과 왼쪽칸 중 최솟값을 더해나간다
for i in range(1,n) :
    for j in range(1,n) :
        arr[i][j] += min(arr[i-1][j],arr[i][j-1])
print(arr[n-1][n-1])

# top-down 풀이

# def dfs(x,y) :
#     if dp[x][y] > 0 :
#         return dp[x][y]
#     if x == 0 and y == 0 :
#         return arr[0][0]
#     else:
#         if x==0 :
#             dp[x][y] = dfs(x,y-1) + arr[x][y]
#         elif y == 0 :
#             dp[x][y] = dfs(x-1,y) + arr[x][y]
#         else :
#             dp[x][y] = min(dfs(x,y-1),dfs(x-1,y)) + arr[x][y]
#     return dp[x][y]
# dfs(n-1,n-1)