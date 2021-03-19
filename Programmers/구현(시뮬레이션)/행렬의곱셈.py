def solution(arr1, arr2):
    # answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    answer = []

    for i in range(len(arr1)):
        lst = []
        for j in range(len(arr2[0])):
            atom = 0
            for k in range(len(arr1[0])):
                atom += (arr1[i][k] * arr2[k][j])
            lst.append(atom)
        answer.append(lst)
    return answer