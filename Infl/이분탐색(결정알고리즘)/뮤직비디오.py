n,m = map(int,input().split())
arr = list(map(int,input().split()))

large = sum(arr)
maxx = max(arr)
lt = 1
rt = large
mid = (lt+rt)//2
res = 0
while lt <= rt :
    mid = (lt+rt) //2
    b = 0
    cnt = 0
    for a in arr :
        if a + b > mid :
            cnt += 1
            b = a
        else :
            b+=a
    # 마지막에 남는 원소들을 한 번 더해야되기에 +1해준다
    cnt +=1

    # 결과값은 항상 원소의 최댓값보다 커야한다
    # 따라서 mid>=maxx 조건 추가
    if mid>= maxx and cnt <= m :
        res = mid
        rt = mid - 1
        # print('rt',rt)
    else :
        lt = mid + 1
        # print('lt',lt)
print(res)
