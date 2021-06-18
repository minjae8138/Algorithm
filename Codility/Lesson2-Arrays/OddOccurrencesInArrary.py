def solution(A):
    # write your code in Python 3.6
    temp = sorted(A)
    answer = []
    for t in temp :
        if answer and t == answer[-1] :
            answer.pop()
        elif t not in answer :
            answer.append(t)
    return answer[0]