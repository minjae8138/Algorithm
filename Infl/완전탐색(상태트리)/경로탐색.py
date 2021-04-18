def dfs(v) :
    global cnt
    if v == n:
        for x in path :
            print(x,end="")
        print()
        cnt+=1
    else :
        for i in range(1,n+1) :
            if matrix[v][i] == 1 and ch[i]==0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0
    return cnt


n,m = map(int,input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m) :
    a,b = map(int,input().split())
    matrix[a][b] = 1
ch[1] = 1
path = []
path.append(1)
cnt = 0
print(dfs(1))
