def isSame(x) :
    if x == x[::-1] :
        return True
    return False

mat = [list(map(int,input().split())) for _ in range(7)]
# mat=[[2, 4, 1, 5, 3, 2, 6],
# [3, 5, 1, 8, 7, 1, 7],
# [8, 3, 2, 7, 1, 3, 8],
# [6, 1, 2, 3, 2, 1, 1],
# [1, 3, 1, 3, 5, 3, 2],
# [1, 1, 2, 5, 6, 5, 2],
# [1, 2, 2, 2, 2, 1, 5]]

cnt = 0
# 길이가 5이고 7x7 행렬이기에 아래와 같이 범위 설정함
for i in range(3) :
    for j in range(7) :
        # 가로 행에 대한 처리
        a = mat[j][i:i+5]
        if isSame(a) :
            cnt +=1
        # 세로 행에 대한 처리
        for k in range(2) :
            if mat[i+k][j] != mat[i+5-k-1][j] :
                break
        else :
            cnt += 1
print(cnt)