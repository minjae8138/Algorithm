n,m = map(int,input().split())
arr = [(idx, val) for idx, val in enumerate(list(map(int,input().split())))]

from collections import deque
dq = deque(arr)
cnt = 0

while True :
    cur = dq.popleft()
    if any(cur[1]<x[1] for x in dq) :
        dq.append(cur)
    else :
        cnt += 1
        if cur[0] == m :
            print(cnt)
            break
