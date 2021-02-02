mat = [list(map(int,input().split())) for _ in range(9)]



# mat = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
# [2, 1, 4, 3, 6, 5, 8, 9, 7],
# [3, 4, 1, 2, 7, 8, 9, 5, 6],
# [4, 3, 2, 1, 8, 9, 6, 7, 5],
# [5, 6, 7, 8, 9, 1, 2, 3, 4],
# [6, 5, 8, 9, 1, 7, 3, 4, 2],
# [7, 8, 9, 5, 2, 3, 4, 6, 1],
# [8, 9, 6, 7, 4, 2, 5, 1, 3],
# [9, 7, 5, 6, 3, 4, 1, 2, 8]]

def isMat(x) :
    # 가로, 세로 처리
    for row in x :
        a= 0
        for i in range(9) :
            a+= row[i]
        if a!= 45 :
            return False
    for i in range(9) :
        a= 0
        for j in range(9) :
            a += mat[j][i]
        if a != 45 :
            False

    # 3X3 행렬 처리
    # 이 방식으로 가로, 세로도 처리할 수 있음
    for i in range(3) :
        for j in range(3) :
            ch3 = [0]*10
            for s in range(3) :
                for k in range(3) :
                    ch3[x[i*3+s][j*3+k]] = 1
            if sum(ch3) != 9 :
                return False
    return True
if isMat(mat) :
    print("YES")
else :
    print("NO")
