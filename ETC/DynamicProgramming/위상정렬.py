n,m = map(int,input().split())
dis = [[5000]*(n+1) for i in range(n+1)]
for i in range(m) :
    a,b = list(map(int,input().split()))
    dis[a][b] = 1
for i in range(n+1) :
    dis[i][i] = 0
for k in range(n+1) :
    for i in range(n+1) :
        for j in range(n+1) :
            dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j])
final = []
for i in range(n+1) :
    temp = []
    for j in range(n+1) :
        temp.append(dis[j][i])
    
    final.append(temp)
final = final[1:]
final = list(map(lambda x : sum(x),final))
for i in range(n) :
    for j in range(n) :
        if final[j] == max(final) :
            print(j+1,end=" ")
            final[j] = 0
            break