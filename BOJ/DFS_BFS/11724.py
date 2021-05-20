# 비슷하지만 틀린 풀이
# cnt를 처리하는 방식 차이

import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
mat = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0 for i in range(n + 1)]
cnt = 0


def dfs(v):
    global cnt
    ch[v] = 1
    for i in range(n + 1):
        if mat[v][i] == 1 and ch[i] == 0:
            dfs(i)
            cnt += 1


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    mat[a][b], mat[b][a] = 1, 1
dfs(1)
print(cnt)

# 정답 풀이
import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
mat = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0 for i in range(n + 1)]
cnt = 0


def dfs(v):
    ch[v] = 1
    for i in range(n + 1):
        if mat[v][i] == 1 and ch[i] == 0:
            dfs(i)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    mat[a][b], mat[b][a] = 1, 1

# dfs 함수 밖에서 처리함으로써 cnt가 원하는대로 연산된다
for i in range(1, n + 1):
    if ch[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)

