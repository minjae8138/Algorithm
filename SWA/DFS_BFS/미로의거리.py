t = int(input())
for T in range(1,t+1) :
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if matrix[i][j] == 2 :
                start_idx = [i,j]

# matrix = [[1,3,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,2,1]]
# start_idx = [4,3]
# n = 5
print(f"start_idx: {start_idx}")
dx = [0,1,-1,0]
dy = [1,0,0,-1]
answer = 0
def bfs(x,y) :
    global answer
    queue = [[start_idx[0],start_idx[1]]]
    queue.append([x,y])
    while queue :
        x,y = queue.pop(0)
        print(f"queue : {queue}")
        # print(f"cnt:{cnt}")
        # print(f"matrix[4][3]: {matrix[4][3]}")
        matrix[start_idx[0],start_idx[1]] = 0
        for i in range(4) :
            ddx = x + dx[i]
            ddy = y + dy[i]          
            if ddx < 0 or ddx > n-1 or ddy <0 or ddy > n-1 :
                continue
            if matrix[ddx][ddy] == 1 :
                continue
            if matrix[ddx][ddy] == 0  :         
                matrix[ddx][ddy] = matrix[x][y] + 1
                # print(matrix[ddx][ddy])
                # print(ddx,ddy)
                queue.append((ddx,ddy))
            if matrix[ddx][ddy] == 3 :
                answer = matrix[x][y]          
    return answer         
print(bfs(start_idx[0],start_idx[1]))


