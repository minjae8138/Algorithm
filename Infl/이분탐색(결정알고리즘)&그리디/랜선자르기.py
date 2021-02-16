k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
# print(arr)

lt = 1
rt = max(arr)
res = 0
while lt<=rt:
    sum = 0
    mid = (lt + rt) // 2
    # print('lt',lt)
    # print('rt',rt)
    for a in arr :
        sum += (a // mid)
    if sum >= n :
        res = mid
        lt = mid+1
    elif sum < n :
        rt = mid-1
print(res)
