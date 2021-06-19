# 이중포문을 안 쓰고 푸는 것이 핵심!
# 시간복잡도 O(N+k)

def solution(N, A):
    answer = [0] * N
    m1 = 0  # N보다 큰 값이 나올 당시의 최댓값
    m2 = 0  # for문 마다의 최댓값
    for a in A :
        if a<= N :
            answer[a-1] = max(answer[a-1]+1,m1+1)
            m2 = max(answer[a-1],m2)
        elif a > N :
            m1 = m2     # m1 업데이트

    # 언급이 안 된 인덱스는 m1으로 변경해주는 작업이 필요
    for i in range(len(answer)) :
        if answer[i] < m1 :
            answer[i] = m1
    return answer