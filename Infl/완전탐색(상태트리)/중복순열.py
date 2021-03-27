# 내가 푼 풀이 - 내장함수 활용

from itertools import product
n,m = map(int,input().split())

a = [a for a in range(1,n+1)]
arr = [a for _ in range(m)]
k = list(product(*arr))

for t in k :
    for i in range(len(t)) :
        print(t[i],end=" ")
    print()
print(len(k))

# dfs 풀이
# m == 트리의 depth

def dfs(l) : # l은 인덱스로 트리를 하나씩 내려가면서 탐색
    global cnt
    if l == m :
        for j in range(m) :
            print(res[j],end=" ")
        print()
        cnt +=1
    else :
        for i in range(1,n+1) :
            res[l] = i
            dfs(l+1)
    return

n, m = map(int, input().split())
res = [0] * (n+1)
cnt = 0
dfs(0)
print(cnt)