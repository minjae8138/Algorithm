n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

answer = 0
for x in range(n) :
    for y in range(n) :
        cnt = 0
        a = [1,0,0,-1]
        b = [0,-1,1,0]
        for i in range(4) :
            dx = x + a[i]
            dy = y + b[i]
            # print(dx,dy)
            if dx < 0 or dx >= n or dy < 0 or dy >= n :
                cnt += 1
                continue
            if matrix[x][y] > matrix[dx][dy] :
                cnt += 1
        if cnt == 4 :
            answer += 1
print(answer)
