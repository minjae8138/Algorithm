# deque의 장점은 시간복잡도이지만
# 이 문제에서는 ans = deque(need)가 아닌
# ans = need로 하고 일반 pop을 사용하면 ans의 형태유지가 되지 않기 때문에
# 반드시 deque를 사용해야 한다
# 왜 deque를 안쓰면 ans 형태가 초기화가 안되는지는 모르겠다..

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

