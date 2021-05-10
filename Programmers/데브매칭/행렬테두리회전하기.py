queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
rows = 6
columns = 6


def solution(rows, columns, queries):
    answer = []
    board = [[] for _ in range(rows)]

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i - 1].append((i - 1) * columns + j)

    for x1, y1, x2, y2 in queries:
        temp = board[x1 - 1][y2 - 1]
        min_value = 10001

        # 북쪽 테두리
        min_value = min(min(board[x1 - 1][y1 - 1:y2 - 1]), min_value)
        board[x1 - 1][y1:y2] = board[x1 - 1][y1 - 1:y2 - 1]

        # 서쪽 테두리
        for i in range(x1, x2):
            min_value = min(board[i][y1 - 1], min_value)
            board[i - 1][y1 - 1] = board[i][y1 - 1]

        # 남쪽 테두리
        min_value = min(min(board[x2 - 1][y1:y2]), min_value)
        board[x2 - 1][y1 - 1:y2 - 1] = board[x2 - 1][y1:y2]

        # 동쪽 테두리
        for i in range(x2 - 2, x1 - 2, -1):
            min_value = min(board[i][y2 - 1], min_value)
            board[i + 1][y2 - 1] = board[i][y2 - 1]

        board[x1][y2 - 1] = temp
        min_value = min(min_value, temp)

        answer.append(min_value)

    return answer


# 첫 번째 풀이시도 - 시간 초과

# import copy
# def solution(rows, columns, queries):
#     answer = []
#     matrix = [[0] * (columns + 2) for _ in range(rows + 2)]
#
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             matrix[i][j] = (i - 1) * columns + j
#
#     retAry = copy.deepcopy(matrix)
#
#     for x1, y1, x2, y2 in queries:
#         min_val = 24700000
#
#         # 맨 위
#         for i in range(y1, y2 + 1) :
#             if i == y1:
#                 retAry[x1][i] = matrix[x1+1][i]
#             else:
#                 retAry[x1][i] = matrix[x1][i - 1]
#             if retAry[x1][i] < min_val :
#                 min_val = retAry[x1][i]
#         # 오른쪽
#         for i in range(x1,x2+1) :
#             if i == x1:
#                 retAry[i][y2] = matrix[i][y2 - 1]
#             else:
#                 retAry[i][y2] = matrix[i - 1][y2]
#             if retAry[i][y2] < min_val:
#                 min_val = retAry[i][y2]
#         # 아래
#         for i in range(y1,y2) :
#             if i == y2:
#                 retAry[x2][i] = matrix[x2 - 1][i]
#             else:
#                 retAry[x2][i] = matrix[x2][i + 1]
#             if retAry[x2][i] < min_val:
#                 min_val = retAry[x2][i]
#         # 왼쪽
#         for i in range(x1,x2):
#             if i == x2:
#                 retAry[i][y1] = matrix[i][y1 + 1]
#             else:
#                 retAry[i][y1] = matrix[i + 1][y1]
#             if retAry[i][y1] < min_val:
#                 min_val = retAry[i][y1]
#         matrix = copy.deepcopy(retAry)
#         print(retAry)
#         answer.append(min_val)
#         print(answer)
#
#     return answer
#
# solution(rows, columns, queries)