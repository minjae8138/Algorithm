n,m = map(int,input().split())

# 내풀이
arr = [i for i in range(1,n+1)]
lst=[]
cnt = 0
while len(arr) > 1 :
    for i in range(len(arr)) :
        cnt += 1
        if cnt % m != 0 :
            lst.append(arr[i])
    arr = lst
    lst = []
print(arr[0])

# deque 사용
from collections import deque

dq = [i for i in range(1,n+1)]
dq = deque(dq)
while dq :
    for i in range(m-1) :
        k = dq.popleft()
        dq.append(k)
    dq.popleft()
    if len(dq) == 1 :
        break
print(dq[0])