top_list = [list(map(int,input())) for _ in range(4)]
t = int(input())
linked = [0]*5


# 하나씩 회전하는 코드
def rotation(lst,r,d) :
    if d == 1 :
        lst[r-1].insert(0,lst[r-1].pop(-1))
    elif d == -1 :
        lst[r-1].append(lst[r-1].pop(0))
        # print(lst[r-1])
    return lst

for _ in range(t) :
    chk = []
    cnt = 0
    def dfs(x) :
        global chk
        global cnt
        cnt += 1
        dx = [-1,0]

        for i in range(2) :
            ddx = x + dx[i]

            if linked[ddx] == 1 :
                linked[ddx] = 0
                chk.append(ddx)
                chk.append(ddx+1)
                dfs(ddx)
        return chk

    r,d = map(int,input().split())
    dfs(r)
    for i in range(3) :
        if top_list[i][2] != top_list[i+1][-2] :
            linked[i+1] = 1
    for c in chk :
        if abs(c - r) % 2 == 0 :
            d = 1
        else :
            d = -1
        rotation(top_list,c,d)



print(top_list[i][0]*1 + top_list[1][0]*2
      + top_list[2][0]*4 + top_list[3][0]*8)




