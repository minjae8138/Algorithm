
t = int(input())
for _ in range(t) :
    k = 0
    result = []
    m,n = map(int,input().split())
    x = int(''.join(map(str,input().split())))
    y = int(''.join(map(str,input().split())))
    lst = list(map(int,input().split()))

    for j in range(m):
        answer = ''
        for i in range(k, k + n):
            answer += str(lst[i % m])
        k += 1
        result.append(answer)

    cnt = 0
    for re in result :
        if int(re) >=x and int(re) <=y :
            cnt +=1
    print(cnt)