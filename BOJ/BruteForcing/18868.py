# 멀티버스I
m,n = map(int, input().split()) # m 우주개수, n 행성개수
space = []
for i in range(m):
    space.append(list(map(int, input().split())))

#행성 간 이동 : a,b
#행성 내 이동 : i,j
answer = 0
for a in range(m-1):
    for b in range(a+1, m): # a 다음 범위부터 탐색
        result = True
        for i in range(n-1):
            for j in range(i+1, n): # i 다음 범위부터 탐색
                if space[a][i] < space[a][j] and space[b][i] >= space[b][j]:
                    result = False
                    break
                elif space[a][i] == space[a][j] and space[b][i] != space[b][j]:
                    result = False
                    break
                elif space[a][i] > space[a][j] and space[b][i] <= space[b][j]:
                    result = False
                    break
        answer += result
print(answer)