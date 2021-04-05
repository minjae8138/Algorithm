
def dfs(l) : # l은 인덱스로, 트리를 하나씩 내려가면서 탐색
    global cnt
    if l == m :
        for j in range(m) :
            print(res[j],end=" ")
        print()
        cnt +=1
    else :
        for i in range(1,n+1) :
            if ch[i]==0 :
                ch[i]=1
                res[l] = i
                dfs(l+1)
                ch[i] = 0
    return

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n+1)
cnt = 0
dfs(0)
print(cnt)