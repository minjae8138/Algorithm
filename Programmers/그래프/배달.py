import math
def solution(N, road, K):
    answer = 0
    visited = []  # 방문체크
    distance = [0] + [math.inf for i in range(1, N)]  # 마을간 이동거리
    roads = {i: {} for i in range(N)}  # 마을과 연결도로 정보 저장

    for r in road:
        # 같은 도로의 경우
        if r[1] - 1 in roads and r[0] - 1 in roads[r[1] - 1]:
            # 기존 거리가 현재 거리보다 값이 클 경우 현재 거리로 변경(업데이트)
            if roads[r[0] - 1][r[1] - 1] > r[2]:
                roads[r[1] - 1][r[0] - 1] = r[2]
                roads[r[0] - 1][r[1] - 1] = r[2]
        else:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    # 첫 번째 마을과 직접 연결된 곳 업데이트
    for i in roads[0]:
        distance[i] = roads[0][i]

    while len(visited) != N:
        small = math.inf
        for i in range(1, N):
            if i not in visited and distance[i] < small:
                small = distance[i]
                town = i
        visited.append(town)
        for i in roads[town]:
            if distance[i] > distance[town] + roads[town][i]:
                distance[i] = distance[town] + roads[town][i]

    for d in distance:
        if d <= K:
            answer += 1

    return answer