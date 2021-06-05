from collections import deque

s,e = map(int,input().split())
jump = [1,-1,5]

q = deque()
q.append(s)

ch = [0] * 1000
while q :
    v = q.popleft()
    for i in range(3) :
        dv = v + jump[i]
        if ch[dv] ==0 and 0<dv <10001 :
            q.append(dv)
            ch[dv] = ch[v] + 1
    if ch[e] != 0 :
        break
print(ch[e])