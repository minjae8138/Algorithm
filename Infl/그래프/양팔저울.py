def dfs(l, sum_) :
    global res
    if l == n :
        if 0<sum_<=s:
            res.add(sum_)

    else :
        dfs(l+1, sum_ + g[l])
        dfs(l+1, sum_ - g[l])
        dfs(l+1, sum_)


n = int(input())
g = list(map(int,input().split()))
s= sum(g)
res = set()
dfs(0,0)
print(s-len(res))