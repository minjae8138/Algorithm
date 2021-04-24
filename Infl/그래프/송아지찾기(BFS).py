n,m = map(int,input().split())
from collections import deque
jump = [1,-1,5]
dis = [0] * 10001
ch = [0] * 10001
q = deque([n])
while True :
    v = q.popleft()
    ch[v] = 1
    for i in range(3) :
        new_v = v + jump[i]
        if ch[new_v] == 0 and 0 < new_v <= 10001:
            ch[new_v] = 1
            dis[new_v] = dis[v] + 1
            q.append(new_v)
    if dis[m] != 0 :
        break
print(dis[m])