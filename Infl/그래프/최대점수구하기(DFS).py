def dfs(l,s,t) :
    global res
    if t > m :
        return
    if l == n :
        print(l,s,t,res)
        if s > res :
            res = s
    else :
        dfs(l+1,s+score[l],t+time[l])
        dfs(l+1,s,t)


n,m = map(int,input().split())
score = list()
time = list()
res = -10000
for _ in range(n) :
    a, b = map(int,input().split())
    score.append(a)
    time.append(b)
dfs(0,0,0)
print(res)

