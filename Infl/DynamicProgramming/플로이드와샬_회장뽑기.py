n = int(input())
dis = [[5000] * (n+1) for i in range(n+1)]
for i in range(5000) :
    a,b = list(map(int,input().split()))
    dis[a][b] = 1
    dis[b][a] = 1
    if a == -1 and b == -1 :
        break
for i in range(n+1) :
    for j in range(n+1) :
        if i == j :
            dis[i][j] = 0
for k in range(n+1) :
    for i in range(n+1) :
        for j in range(n+1) :
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(n+1) :
    for j in range(n+1) :
        if dis[i][j] == 5000 :
            dis[i][j] = 0
dis = dis[1:]
lst = []
for d in dis :
    d = max(d)
    lst.append(d)
print(min(lst),lst.count(min(lst)),end=" ")
print()
for i in range(len(lst)) :
    if lst[i] == min(lst) :
        print(i+1,end= " ")

