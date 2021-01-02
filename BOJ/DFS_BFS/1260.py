# 기본 dfs, bfs 구현 문제
n,m,v = map(int,input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m) :
    x,y = map(int,input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
    
def dfs(x) :
    print(x,end=" ")
    visited[x] = 1
    for i in range(1,n+1) :
        if matrix[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
# dfs 연산 과정에서 visited의 값들이 변경되었기에 이를 고려해야함
# visited[x] = 1 일 때가 방문x, 0일 때가 방문o 으로 변경하여 품
def bfs(x) :
    queue = [x]
    visited[x] = 0 
    while queue :
        x = queue.pop(0)
        print(x,end=" ")
        for i in range(1,n+1) :
            if matrix[x][i] == 1 and visited[i] == 1:
                queue.append(i)
                visited[i] = 0                           
dfs(v)
print()
bfs(v)