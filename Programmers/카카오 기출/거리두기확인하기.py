from itertools import combinations


def solution(places):
    answer = []

    for place in places:
        res = []
        tmp = []
        chk = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    res.append((i, j))
        combs = list(combinations(res, 2))
        for comb in combs:
            k = abs(comb[0][0] - comb[1][0]) + abs(comb[1][0] - comb[1][1])
            if k <= 2:
                if abs(comb[0][0] - comb[1][0]) > 0:
                    if place[min(comb[0][0], comb[1][0]) + 1][comb[0][1]] == "X":
                        chk = 1
                    else:
                        chk = 0
                if abs(comb[0][1] - comb[1][1]) > 0:
                    if place[comb[0][0]][min(comb[0][1], comb[1][1])] == "X":
                        chk = 1
                    else:
                        chk = 0
            else:
                chk = 1
        answer.append(chk)
    return answer