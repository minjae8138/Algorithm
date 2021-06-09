import copy
from collections import deque

n = int(input())
matrix = [list(map(int,input()))for _ in range(n)]

ret = copy.deepcopy(matrix)
dx = [0,1,0,-1]
dy = [-1,0,1,0]
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
                for k in range(4) :
                    ddx = x + dx[k]
                    ddy = y + dy[k]
                    if 0<=ddx<n and 0<=ddy<n and ret[ddx][ddy] == 1 :
                        q.append((ddx,ddy))
                        ret[ddx][ddy] = 0
            res.append(cnt)
print(len(res))
for r in sorted(res) :
    print(r)
