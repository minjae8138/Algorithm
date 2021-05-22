

n = int(input())
mat = [list(map(int,input().split())) for x in range(n)]

# bfs 안 쓴 나의 풀이
# 문제 의도와는 다르지만 더 효율적인 풀이 같음(시간복잡도가 더 낮음)

matAry = mat[:]
idx = 1
row = 0
mid = n // 2
s = mid
tot = 0
while row < n:
    # print(matAry[row][s:s + idx])
    tot += sum(matAry[row][s:s + idx])
    if row < mid :
        idx += 2
        s -= 1
    else :
        idx -= 2
        s+=1
    row += 1
print(tot)


# bfs
# from collections import deque

# x, y = n//2, n//2
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# ch = [[0] * n for _ in range(n)]
#
# q = deque([[x,y]])
# tot = mat[x][y]
# level = 0
# while q :
#     print("level : ",level)
#     if level == n//2 :
#         break
#
#     size = len(q)
#     ch[x][y] = 1
#
#     for k in range(size) :
#         v = q.popleft()
#         x, y = v[0], v[1]
#         for i in range(4) :
#             ddx = x + dx[i]
#             ddy = y + dy[i]
#             if ddx >=0 and ddx < n and ddy >= 0 and ddy < n and ch[ddx][ddy] == 0:
#                 ch[ddx][ddy] = 1
#                 print(mat[ddx][ddy])
#                 tot += mat[ddx][ddy]
#                 q.append([ddx,ddy])
#     level += 1
#
# print(tot)







