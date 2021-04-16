def dfs(l,s) :
    global cnt
    if l == k :
        sum = 0
        for i in range(k) :
            sum += res[i]
        if sum % m == 0 :
            cnt +=1
    else :
        for i in range(s,n) :
            res[l] = arr[i]
            dfs(l+1, i+1)
    return cnt


n,k = map(int,input().split())
arr = list(map(int,input().split()))
m = int(input())
res = [0] * n
cnt = 0
print(dfs(0,0))