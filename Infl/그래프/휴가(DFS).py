def dfs(l,t,p) :    # l : 노드 길이, t : time, p : pay
    global res
    if t > n or l > n:
        return
    if l == n :
        # print(l,t,p,res)
        if p > res :
            res = p
    else :
        if l+times[l] <=n :
            # print("before : ",l,t,p,res)
            dfs(l+times[l], t+times[l], p+pays[l])
        dfs(l+1,t,p)

n = int(input())
temp  = [list(map(int,input().split())) for _ in range(n)]
times = list(map(lambda x:x[0],temp))
pays  = list(map(lambda x:x[1],temp))

res = -10000
dfs(0,0,0)
print(res)


# def dfs(l,sum_) :
#     global res
#     if l == n+1 :
#         if sum_ > res :
#             res = sum_
#     else :
#         if l + pt[l] <= n+1 :
#             dfs(l+pt[l],sum_+pv[l])
#         dfs(l+1,sum_)
#
# n = int(input())
# pt = list()
# pv = list()
# for _ in range(n) :
#     a,b = map(int,input().split())
#     pt.append(a)
#     pv.append(b)
# pv.insert(0,0)
# pt.insert(0,0)
# res = -1000000
# dfs(1,0)
# print(res)