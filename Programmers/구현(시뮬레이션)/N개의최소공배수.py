def solution(arr):

    def gcd(x,y) :
        while y :
            x,y = y,x%y
        return x

    def lcm(x,y) :
        return x * y // gcd(x,y)

    res = []
    for a in arr :
        if res :
            res.append(lcm(res.pop(-1),a))
        else :
            res.append(a)

    return res[0]

    # 11 ~ 18 코드 while문으로 푸는 방법
    # while 1 :
    #     arr.append(lcm(arr.pop(),arr.pop()))
    #     if len(arr) == 1 :
    #         return res[0]

