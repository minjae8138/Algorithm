def dfs(l,s) :
    global cnt
    if l==m :
        for i in range(m) :
            print(res[i],end=" ")
        print()
        cnt+=1
    else :
        for i in range(s,n+1) :  # 조합이어서 범위가 이전값인 s부터
            res[l] = i
            dfs(l+1, i+1)
n,m = map(int,input().split())
res = [0] *(n+1)
cnt = 0
dfs(0,1)
print(cnt)