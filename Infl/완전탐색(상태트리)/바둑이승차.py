weight, n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
max_val = 0

def dfs(l, sum, tsum):
    global max_val

    # 남아있는 트리를 더하고 현재 max_val보다 작으면 더 계산할필요가 없음
    if sum + (total - tsum) < max_val:  # cut edge
        return

    if sum > weight:  # cut edge
        return
    if l == n:
        if sum < weight:
            if sum > max_val:
                max_val = sum
        # print(max_val)
        return max_val
    else:
        dfs(l + 1, sum + arr[l], tsum + arr[l])
        dfs(l + 1, sum, tsum + arr[l])
    return max_val

total = sum(arr)
print(dfs(0, 0, 0))