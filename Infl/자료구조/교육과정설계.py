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

