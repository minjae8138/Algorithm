def solution(A, K):
    # write your code in Python 3.6
    if not A :
        return []
    else :
        for _ in range(K):
            A.insert(0, A.pop())
    return A