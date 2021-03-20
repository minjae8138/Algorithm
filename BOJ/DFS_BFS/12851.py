
from collections import deque

def bfs(v):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        v = q.popleft()
        e = v[0]
        cnt = v[1]
        if visited[e] == 0:
            visited[e] = 1
            if e == b:
                return cnt
            cnt += 1

            if (e * 2) <= 100000:
                q.append([e * 2, cnt])
            if (e + 1) <= 100000:
                q.append([e + 1, cnt])
            if (e - 1) >= 0:
                q.append([e - 1, cnt])

    return cnt

a, b = map(int, input().split())
visited = [0] * 100001
print(bfs(a))


# 이전 풀이와 같은 bfs지만
# 좀 더 간결하게 풀었다
# bfs 함수의 인자 최소화
# cnt 변수를 따로 만들지 않음

# from collections import deque
cur, target = map(int, input().split())

q = deque()
q.append(cur)
visit = [0] * 100001
large = 100001

def bfs():
    while q:
        pos = q.popleft()
        if pos == target:
            break
        for next in (pos + 1, pos - 1, pos * 2):
            if 0 <= next < large and not visit[next]:
                visit[next] = visit[pos] + 1
                q.append(next)
    return visit[pos]
print(bfs())
