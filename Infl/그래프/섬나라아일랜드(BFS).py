# bfs
# 시간효율성 아슬아슬하게 통과
# deepcopy를 사용하면 1번째 케이스에서 time limit 걸림
import time
start = time.time()
from collections import deque

n = int(input())
ret = [list(map(int,input().split()))for _ in range(n)]

# 대각선까지 포함되어서 8개의 방위를 표현
dx = [0,1,0,-1,1,1,-1,-1]
dy = [-1,0,1,0,-1,1,1,-1]

res = []
q = deque()
for i in  range(n) :
    for j in range(n) :
        if ret[i][j] == 1 :
            q.append((i,j))
            ret[i][j] = 0
            cnt = 0
            while q :
                cnt += 1
                v = q.popleft()
                x = v[0]
                y = v[1]
                for k in range(8) :
                    ddx = x + dx[k]
                    ddy = y + dy[k]
                    if 0<=ddx<n and 0<=ddy<n and ret[ddx][ddy] == 1 :
                        q.append((ddx,ddy))
                        ret[ddx][ddy] = 0
            res.append(cnt)
print(len(res))
last = time.time()
print(last-start)

