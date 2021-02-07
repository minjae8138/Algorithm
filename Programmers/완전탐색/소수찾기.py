# 보자마자 permutations가 떠올라서 itertools 함수를 사용했다
# n이 정해져 있지 않아서 이를 처리하고 알맞게 형식변환을 하는 것이 중요했다
# 다른 풀이를 보니 itertools를 사용하지 않고 풀거나, set을 활용하여 푼 풀이도 있었다
# set을 활용한 풀이는 충격적...(여러 번 봐야 될거같다)

## 나의풀이
from itertools import permutations
def solution(numbers):
    comb = []
    for i in range(1, len(numbers) + 1):
        for j in list(permutations(numbers, i)):
            comb.append(list(j))
    # print(comb)
    lst = []
    for com in comb:
        com = ''.join(com)
        lst.append(com)
    answer = list(map(int, lst))
    answer = list(set(answer))

    def isprime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    cnt = 0
    for a in answer:
        # print(a)
        if a > 1 and isprime(a):
            cnt += 1
    return cnt

## 다른풀이
# set 활용
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 비트마스크
    a -= set(range(0, 2))

    # 에라토스테네스체의 set 버전
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)