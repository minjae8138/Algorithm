def dfs(l,sum_) :
    global cnt
    if l == k :
        if sum_ == t :
            cnt += 1
    else :
        for i in range(cn[l]+1) :
            dfs(l+1,sum_ + cv[l]*i)


t = int(input())
k = int(input())
cv=list()
cn=list()
for _ in range(k) :
    p,n = map(int,input().split())
    cv.append(p)
    cn.append(n)
cnt = 0
dfs(0,0)
print(cnt)
