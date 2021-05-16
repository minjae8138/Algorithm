# 3진수구하는 것과 유사 (0이 4로 바뀌는 것)

# 내 풀이
def solution(n):
    answer = []
    while 1:
        if n <= 3:
            answer.append(("124"[n - 1]))
            break
        else:
            n, r = divmod(n - 1, 3)
            answer.append(("124"[r]))

    answer = "".join(answer[::-1])

    return answer

# 다른 사람 풀이
# 재귀 활용
def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]


