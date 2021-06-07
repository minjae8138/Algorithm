import copy

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

ret = copy.deepcopy(matrix)
large = -2470000
small = 2470000

# 최댓값, 최솟값 좌표 구하기
for i in range(len(ret)):
    for j in range(len(ret[i])):
        if ret[i][j] < small:
            small = ret[i][j]
            small_x, small_y = i, j
        if ret[i][j] > large:
            large = ret[i][j]
            large_x, large_y = i, j
# print(small_x,small_y,large_x,large_y)

ch = [[0] * n for _ in range(n)]
ch[small_x][small_y] = 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0

# dfs
def dfs(x, y):
    global cnt
    if ch[large_x][large_y] == 1:
        cnt += 1
    else:
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < n and 0 <= ddy < n and ret[ddx][ddy] > ret[x][y] and ch[ddx][ddy] == 0:
                ch[ddx][ddy] = 1
                dfs(ddx, ddy)
                ch[ddx][ddy] = 0        # 뒤로가기

dfs(small_x, small_y)
print(cnt)