n = int(input())
time = []
money = []
for i in range(n) :
    a,b = map(int,input().split())
    time.append(a)
    money.append(b)

large = 0
def dfs(l,m) :
    global large
    if l == n :
        if m > large :
            large = m
            return large
    else :
        if l+time[l] <= n :
            dfs(l+time[l],m+money[l])
        dfs(l+1,m)

dfs(0,0)
print(large)





















