import copy
n = 10
matrix = [list(map(int,input().split())) for _ in range(n)]
ret = copy.deepcopy(matrix)
ch = [[0]*n for _ in range(n)]

# 2를 가지는 값으로부터 위로 거슬러가기에 아래로 가는코드는 필요없다
# 또한 양옆을 우선으로 탐색(사디리타기 특성상 좌우에 길이 있으면 거기로 가야함)
dx = [0,0,-1]
dy = [1,-1,0]

res = []
def dfs(x,y) :
    global res
    ch[x][y] = 1
    if x == 0 :
        res.append(y)       # 아래 for문의 dfs때문에 계속해서 동작하기 때문에 res 변수에 담아서 슬라이싱하는 작업이 필요
                            # exit를 통해 아예 종료할 수도 있음
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