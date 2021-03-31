def dfs(l,sum) : # l은 인덱스로 트리를 하나씩 내려가면서 탐색[l이 cnt로 보면 된다]
    global min_cnt
    if sum > target :
        return
    if l > min_cnt :
        return
    if  sum == target :
        if l < min_cnt :
            min_cnt = l


    else :
        for i in range(n) :
            dfs(l+1, sum+coin[i])
    return min_cnt

n = int(input())
coin = list(map(int,input().split()))
coin.sort(reverse=True)
target = int(input())
min_cnt = 500
print(dfs(0,0))
