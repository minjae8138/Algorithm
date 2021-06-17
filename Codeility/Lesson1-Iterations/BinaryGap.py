def solution(N):
    # write your code in Python 3.6
    num = bin(N)[2:]
    res = 0
    cnt = 0
    for n in num :
        if int(n) == 0 :
            cnt += 1
        elif int(n) == 1 :
            if res < cnt :
                res = cnt
            cnt = 0
    return max(res)
