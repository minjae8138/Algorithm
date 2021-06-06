from collections import deque
import copy

matrix = [list(map(int, input().split())) for _ in range(7)]

ch = [[0] * 7 for _ in range(7)]
ret = copy.deepcopy(matrix)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append([0, 0])
ret[0][0] = 1

while q:
    v = q.popleft()
    x, y = v[0], v[1]
    cnt = 0
    for i in range(4):
        ddx = x + dx[i]
        ddy = y + dy[i]
        if ddx >= 0 and ddx < 7 and ddy >= 0 and ddy < 7 and ret[ddx][ddy] == 0:
            cnt += 1
            ret[ddx][ddy] = 1
            ch[ddx][ddy] = ch[x][y] + 1
            q.append([ddx, ddy])
if ch[6][6] == 0 :
    print(-1)
else :
    print(ch[6][6])
