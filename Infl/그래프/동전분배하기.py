def dfs(l) :
    global res
    if l == n :
        if max(people) - min(people) < res :
            temp = set()
            for i in range(3) :
                temp.add(people[i])
            if len(temp)==3 :
                res = max(people) - min(people)
                print(res)

    else :
        for i in range(3) :
            people[i]+=arr[l]
            dfs(l+1)
            people[i]-=arr[l]   # 이전 가지로 돌아가는 경우 다시 빼준다



n = int(input())
arr = list(map(int,input().split()))
people = [0] * 3
res = 24700000
dfs(0)
print(res)
