import copy
from collections import deque

n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
ret = copy.deepcopy(matrix)
dis = [[0]*n for _ in range(m)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 우선 행렬에서 1인 값(토마토)들에 대해 q에 추가
q = deque()
for i in range(m) :
    for j in range(n) :
        if ret[i][j] == 1 :
            q.append((i,j))
# bfs
while q :
    tmp = q.popleft()
    for k in range(4) :
        ddx = tmp[0] + dx[k]
        ddy = tmp[1] + dy[k]
        if 0<=ddx<m and 0<=ddy<n and ret[ddx][ddy] == 0 and dis[ddx][ddy] ==0:
            ret[ddx][ddy] = 1
            dis[ddx][ddy] = dis[tmp[0]][tmp[1]] + 1
            q.append((ddx,ddy))

# 다 익지 못하는 경우 처리(-1)
flag = 0
for i in range(m) :
    for j in range(n) :
        if ret[i][j] == 0 :
            flag = -1

# 다 익는데 걸리는 시간(최댓값 찾기)구하기
large = -2470000
for i in range(m):
    for j in range(n):
        if dis[i][j] > large:
            large = dis[i][j]
if flag == 0 :
    print(large)
else :
    print(-1)



