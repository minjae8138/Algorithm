def dfs(l,s) :
    global answer
    if l == k :
        if s == t :
            answer += 1
    else :
        for i in range(cnt[l]+1) :
            dfs(l+1,s+pay[l]*i)

t = int(input())
k = int(input())
pay = list()
cnt = list()
for _ in range(k) :
    a,b = map(int,input().split())
    pay.append(a)
    cnt.append(b)
answer = 0
dfs(0,0)
print(answer)

