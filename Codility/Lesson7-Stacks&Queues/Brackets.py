def solution(S):
    if S == [] :
        return 1
    stack = []

    for s in S :

        if stack and ((stack[-1] == '(' and s==')') or stack[-1] =='{' and s=='}' or stack[-1] == '[' and s==']') :
            stack.pop(-1)
        else :
            stack.append(s)

    if stack :
        return 0
    else :
        return 1