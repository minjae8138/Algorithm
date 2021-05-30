def dfs(l,s,t) :  # l : 노드 길이, s : 점수 합
    global res
    if t > m :
        return
    if l == n :
        print(l, s, t, res)
        if s > res :
            res = s
        print("res : ",res)
        return res
    else :
        dfs(l+1, s+scores[l],t+times[l])
        dfs(l+1, s, t)

n,m = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
res = -10000

scores = list(map(lambda x: x[0], temp))
times  = list(map(lambda x: x[1], temp))

dfs(0,0,0)
print(res)