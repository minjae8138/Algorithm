def solution(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a % 1234567

# 재귀함수보다 for문이 더 효율적임
# 그중에서도 위와 같이 제너레이터 형식으로 푸는 것이 메모리 효율성이 좋음