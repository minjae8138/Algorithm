# 순열
import sys
def dfs(l,sum) :
    # 합계가 f일때 출력 후 종료
    if l == n and sum==f:
        for r in res :
            print(r, end=" ")
        sys.exit(0) # 프로그램 종료, 이 경우 dfs의 재귀때문에 return으로 종료가 안되어서 필요함

    else :
        for i in range(1,n+1) :
            if ch[i] ==0 :
                ch[i]=1
                res[l] = i
                dfs(l+1,sum+res[l]*c[l])
                ch[i]=0
    return

n,f = map(int,input().split())
res = [0] * n

# 파스칼의 합에서는 처음 노드에서 n-1Cr만큼 곱한수가 최종합
# n = 4 면 1 3 3 1 -> 3C0 3C1 3C2 3C3
c = [1] * n # 항상 처음과 끝은 1
for i in range(1,n) :
    c[i] = (c[i-1]*(n-i)) // i  # 분자는 하나씩 작아지는 값을 곱하고(n-i) 분모는 하나씩 커지는 값인 i만큼 나누면 된다
ch = [0] * (n+1)
dfs(0,0)


