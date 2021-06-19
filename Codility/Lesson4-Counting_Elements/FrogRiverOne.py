def solution(X, A):
    # write your code in Python 3.6
    answer = [0] * (X + 1)
    cnt = 0
    for i in range(len(A)):
        if answer[A[i]] == 0:
            answer[A[i]] = 1
            cnt += 1
            if cnt == X:
                return i

    return -1