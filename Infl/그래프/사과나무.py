# bfs

from collections import deque

n = int(input())
mat = [list(map(int,input().split())) for x in range(n)]
x, y = n//2, n//2       # 행렬의 정중앙 좌표
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ch = [[0] * n for _ in range(n)]

q = deque([[x,y]])
tot = mat[x][y]
level = 0       # 가지가 뻗어나가는 단계 l
while q :
    print("level : ",level)
    if level == n//2 :
        break

    size = len(q)
    ch[x][y] = 1

    for k in range(size) :
        v = q.popleft()
        x, y = v[0], v[1]
        for i in range(4) :
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx >=0 and ddx < n and ddy >= 0 and ddy < n and ch[ddx][ddy] == 0:
                ch[ddx][ddy] = 1
                print(mat[ddx][ddy])
                tot += mat[ddx][ddy]
                q.append([ddx,ddy])
    level += 1

print(tot)







