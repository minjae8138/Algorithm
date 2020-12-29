
def dfs(x) :
        visit.append(x)
        for i in range(1,v+1) :
            if matrix[x][i] == 1 :
                dfs(i)
t = int(input())
for T in range(1,t+1) :
    v,e = map(int,input().split())
    matrix = [[0] * (v+1) for _ in range(v+1)]
    for _ in range(e) :
        x,y = map(int,input().split())
        matrix[x][y] = 1
    s,g = map(int,input().split())
    visit = []
    dfs(s)
    if g in visit :
        print(f"#{T} 1")
    else :
        print(f"#{T} 0")
