n = int(input())
mat = [list(map(int,input().split())) for x in range(n)]

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