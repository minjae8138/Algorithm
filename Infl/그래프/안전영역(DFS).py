import copy

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
ret = copy.deepcopy(matrix)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def dfs(x,y) :
    ret[x][y] = 0
    for i in range(4) :
        ddx = x + dx[i]
        ddy = y + dy[i]
        if 0<=ddx<n and 0<=ddy<n and ret[ddx][ddy] != 0 :
            dfs(ddx,ddy)

large = 0
for i in range(n) :
    for j in range(n) :
        if ret[i][j] >large :
            large = ret[i][j]

res = []
for t in range(1,large) :
    ret = copy.deepcopy(matrix)
    for i in range(n) :
        for j in range(n) :
            if ret[i][j] <= t :
                ret[i][j] = 0
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if ret[i][j] != 0 :
                cnt +=1
                dfs(i,j)
    res.append(cnt)

print(max(res))