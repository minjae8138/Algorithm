def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution(q) + '124'[r]


# 3진수구하는 것과 유사