weight, n = map(int,input().split())
arr = [int(input()) for _ in range(n)]
# print(weight,n,arr)
max_val = 0
def dfs(l,sum) :
    global max_val
    if sum > weight :
        return

    if l == n :

        if sum < weight :
            if sum > max_val :
                max_val = sum
        # print(max_val)
        return max_val
    else :
        dfs(l+1, sum+arr[l])
        dfs(l+1, sum)
    return max_val

print(dfs(0,0))