def dfs(l,sum_) :
    global res
    if l == n+1 :
        if sum_ > res :
            res = sum_

    else :
        if l + pt[l] <= n+1 :
            dfs(l+pt[l],sum_+pv[l])
        dfs(l+1,sum_)

n = int(input())
pt = list()
pv = list()
for _ in range(n) :
    a,b = map(int,input().split())
    pt.append(a)
    pv.append(b)
pv.insert(0,0)
pt.insert(0,0)
res = -1000000
dfs(1,0)
print(res)