def dfs(l,s) :
    if l == n :
        if 0<s<=sum(arr) :
            ch.add(s)
    else :
        # 더할 때, 뺄 때, 그대로일 때
        dfs(l+1,s+arr[l])
        dfs(l+1,s-arr[l])
        dfs(l+1,s)

n = int(input())
arr = list(map(int,input().split()))
ch = set()  # 리스트보다 빠르게 접근(해쉬방식)
dfs(0,0)
print(sum(arr)-len(ch))