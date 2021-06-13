import copy
from collections import deque

dx = [0,1,0,-1]
dy = [-1,0,1,0]
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
ret = copy.deepcopy(matrix)

# 행렬(주어진 지역)에서 최댓값(최대높이)구하기
large = -2470000
for row in ret :
    for r in row :
        if r > large :
            large = r
large = large - 1       # 최댓값으로 하면 모든 지역이 잠기므로 굳이 비교할 필요가 없다(large-1까지)

# 물에 잠기는 지역은 0으로 변환
res = []        # 높이별 안전영역 수(cnt)가 담길 최종 리스트
q = deque()     # 어차피 while문에서 나오면 빈 값이어서 위치는 중요치 않다(24번째 줄 다음에 넣어도됨)
for t in range(1,large) :
    ret = copy.deepcopy(matrix)     # t가 바뀔때마다 행렬이 초기화 시켜줌
    for i in range(n) :
        for j in range(n) :
            if ret[i][j] <= t :
                ret[i][j] = 0

    # bfs
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if ret[i][j] != 0 :
                q.append((i,j))
                cnt += 1
                while q :
                    temp = q.popleft()
                    for k in range(4) :
                        x = temp[0] + dx[k]
                        y = temp[1] + dy[k]
                        if 0<=x<n and 0<=y<n and ret[x][y] != 0 :
                            q.append((x,y))
                            ret[x][y] = 0
    res.append(cnt)

print(max(res))

