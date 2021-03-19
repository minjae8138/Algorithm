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