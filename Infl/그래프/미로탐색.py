# dfs / back tracking

import copy
matrix = [list(map(int,input().split())) for _ in range(7)]
ret = copy.deepcopy(matrix)
dx = [0,1,0,-1]
dy = [-1,0,1,0]
cnt = 0

def dfs(x,y) :
    global cnt
    if x == 6 and y == 6  :
        cnt += 1
    else :
        for i in range(4) :
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0<=ddx<7 and 0<=ddy<7 and ret[ddx][ddy] ==0 :
                ret[ddx][ddy] = 1
                dfs(ddx,ddy)
                ret[ddx][ddy] = 0       # 생각지 못한 핵심코드
                                        # 가지가 되돌아갈때 앞의 값을 초기화해주는 부분
                                        # 길(0)을 벽(1)으로 바꿨으니 이를 다시 길(0)로 바꾸는 과정

ret[0][0] = 1
dfs(0,0)
print(cnt)