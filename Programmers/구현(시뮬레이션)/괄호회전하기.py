def solution(s):
    # 문자열이 올바른 괄호 문자열인지 아닌지 판별하는 함수
    # 올바르면 True 리턴
    # 올바르지 않으면 False 리턴
    def check(s):
        ch = []
        for i in s:
            if ch and ((ch[-1] == "[" and i == "]") or (ch[-1] == "{" and i == "}") or
                       (ch[-1] == "(" and i == ")")):
                ch.pop()
            else:
                ch.append(i)
        if ch == []:
            return True
        else:
            return False

    # s에 대해서 각각 회전한 값에 대한 check를 하면서 True면 카운트 + 1
    x = len(s)
    answer = 0
    for i in range(x):
        if check(s):
            answer += 1
        first = s[0]
        s = s[1:]
        s += first

    return answer