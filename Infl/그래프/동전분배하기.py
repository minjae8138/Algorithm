def dfs(l) :
    global res
    if l == n :

        if max(money) - min(money) < res :
            tmp = set()
            for x in money :
                tmp.add(x)
            if len(tmp) == 3 :
                res = max(money) - min(money)
                print(money)
    else :
        for i in range(3) :
            money[i] += arr[l]
            dfs(l+1)
            money[i] -= arr[l] # 이전 가지로 돌아가는 경우 다시 빼주는 코드


n = int(input())
arr = list()
for _ in range(n) :
    a = int(input())
    arr.append(a)
money = [0] * 3
res = 24700000
dfs(0)
print(res)