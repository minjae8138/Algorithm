import copy
n = 10
matrix = [list(map(int,input().split())) for _ in range(n)]
ret = copy.deepcopy(matrix)
ch = [[0]*n for _ in range(n)]
dx = [0,0,-1]
dy = [1,-1,0]

res = []
def dfs(x,y) :
    global res
    ch[x][y] = 1
    if x == 0 :
        res.append(y)

    else :
        for i in range(3) :
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0<=ddx<n and 0<=ddy<n and ret[ddx][ddy] == 1 and ch[ddx][ddy] == 0:
                dfs(ddx,ddy)

for i in range(n) :
    for j in range(n) :
        if ret[i][j] == 2 :
            # print(i,j)
            dfs(i,j)

print(res[0])