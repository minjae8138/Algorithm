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