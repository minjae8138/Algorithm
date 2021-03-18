def solution(clothes):
    answer = 1
    hashed = {}
    for cloth in clothes :
        hashed[cloth[1]] = hashed.get(cloth[1],0) + 1
    for value in hashed.values() :
        answer *= (value+1)
    return answer - 1    # 전체가 없는 경우를 제외