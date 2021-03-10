# deque의 장점은 시간복잡도이지만
# 이 문제에서는 ans = deque(need)가 아닌
# ans = need로 하고 일반 pop을 사용하면 ans의 형태유지가 되지 않기 때문에
# 반드시 deque를 사용해야 한다
# 왜 deque를 안쓰면 ans 형태가 초기화가 안되는지는 모르겠다..
# 원인 찾음!

from collections import deque

need = input()
n = int(input())
for t in range(1,n+1) :
    answer = "YES"
    sub = list(map(str,input()))
    ans = deque(need)
    for x in sub :
        if x in ans :
            if x != ans.popleft() :
                answer="NO"
                break
    if ans :
        answer="NO"

    print("#{} {}".format(t,answer))


# 일반 리스트 접근
# 해결

need = input()
n = int(input())
for t in range(1,n+1) :
    answer = "YES"
    sub = list(map(str,input()))

    ans = list(need)
    # ans = need 로 하면 need = ans 랑 같은 코드이기에 원본인
    # need에도 변화가 그대로 적용
    # 따라서 ans = list(need) 처럼 원본과는 다른 값으로 초기화를 하는 것이 옳음
    for x in sub :
        if x in ans :
            if x != ans.pop(0) :
                answer="NO"
                break
    if ans :
        answer="NO"

    print("#{} {}".format(t,answer))
