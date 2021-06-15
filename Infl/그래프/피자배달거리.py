import copy
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
city = copy.deepcopy(matrix)

hs = []     # 집
pz = []     # 피자집
cb = [0] * m
res = 24700000
for i in range(n) :
    for j in range(n) :
        if city[i][j] == 1 :
            hs.append((i,j))
        elif city[i][j] == 2 :
            pz.append((i,j))

print(hs)
print(pz)

def dfs(l,s) :
    global res
    if l == m :
        tot= 0      # 도시의 피자배달 거리
        for i in range(len(hs)) :
            x1 = hs[i][0]
            y1 = hs[i][1]
            dis = 24700000      # 집별 피자배달 거리
            for c in cb :
                x2 = pz[c][0]
                y2 = pz[c][1]
                dis = min(dis,abs(x1-x2) + abs(y1-y2))
            tot += dis
        if tot <= res :
            res = tot

    else :
        # 피자집의 조합구하기
        for i in range(s, len(pz)) :
           cb[l] = i
           dfs(l+1, i+1)

dfs(0,0)
print(res)
