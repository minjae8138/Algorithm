def check(p):
    chk = []
    for k in p:
        if chk and chk[-1] == "(" and k == ")":
            chk.pop()
        else:
            chk.append(k)
    return chk


def divide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        elif p[i] == ")":
            right += 1
        if left == right:
            u = p[:i + 1]
            v = p[i + 1:]
            return u, v


def solution(p):
    # 조건1
    if not p:
        return ""

    # 조건2
    u, v = divide(p)

    # 조건3
    if check(u) == []:
        # 조건3-1
        return u + solution(v)

    # 조건4
    else:
        # 조건4-1
        answer = "("
        # 조건4-2
        answer += solution(v)
        # 조건4-3
        answer += ")"
        # 조건4-4
        for i in range(len(u)):
            if i == 0 or i == (len(u) - 1):
                continue
            if u[i] == "(":
                answer += ")"
            elif u[i] == ")":
                answer += "("
    # 조건4-5
    return answer