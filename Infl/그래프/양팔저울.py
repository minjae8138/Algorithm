def dfs(l, sum_) :
    global res
    if l == n :
        if 0<sum_<=s:
            # print(f'l:{l},sum:{sum_}')
            res.add(sum_)

    else :
        # 더할 때, 뺄 때, 그대로일 때
        dfs(l+1, sum_ + g[l])
        dfs(l+1, sum_ - g[l])
        dfs(l+1, sum_)

n = int(input())
g = list(map(int,input().split()))
s= sum(g)
res = set() # 리스트보다 빠르게 접근(해쉬방식)
dfs(0,0)
print(s-len(res))