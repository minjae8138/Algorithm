# dfs
# bfs보다 3초정도 빠르다

n = int(input())
ret = [list(map(int,input().split()))for _ in range(n)]

dx = [0,1,0,-1,1,1,-1,-1]
dy = [-1,0,1,0,-1,1,1,-1]
res = []

def dfs(x,y) :
    global cnt
    cnt += 1
    ret[x][y] = 0
    for i in range(8) :
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0<=ddx<n and 0<=ddy<n and ret[ddx][ddy] == 1 :
            dfs(ddx,ddy)

res = []
for i in range(n) :
    for j in range(n) :
        if ret[i][j] == 1 :
            cnt = 0
            dfs(i,j)
            res.append(cnt)

print(len(res))


