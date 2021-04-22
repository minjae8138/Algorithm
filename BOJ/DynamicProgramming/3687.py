import math

# 최솟값이 주요 포인트!!!
# 7 이후로는 두 자리 숫자가 나오고 있기에 여기까지의 값을 입력하고
# 이후로는 for문을 통해 앞의 범위만큼 각 값을 비교해서 최솟값을 찾는다
# dp[i] = min(dp[i], dp[i - j] * 10 + num[j])
# 한 자리씩 증가하기에 10을 곱하고 해당 개수에 대한 값(num[j])을 더해준다
# 그 중에서 최솟값을 찾아준다
def DFS_MAX(k):
    if k == 2 or k == 3:
        return dic[k][0]
    if dp[k] == 0:
        dp[k] = DFS_MAX(k - 2) * 10 + DFS_MAX(2)
    return dp[k]


def DFS_MIN(k):
    num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
    dp = [0] * 101
    for i in range(1, 9):
        dp[i] = num[i]
    dp[6] = 6
    for i in range(9, k + 1):
        dp[i] = math.inf
        # print("dp[i]---->",i,dp[i])
        for j in range(2, 8):
            # print("~~~~~~",i-j,dp[i - j] * 10 + num[j])
            dp[i] = min(dp[i], dp[i - j] * 10 + num[j])
    return dp[k]


if __name__ == "__main__":
    n = int(input())
    dic = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}
    dp = [0] * 101

    for _ in range(n):
        k = int(input())
        print(DFS_MIN(k), end=' ')
        print(DFS_MAX(k))



# 내 풀이 - 규칙을 찾아서 해결 -> dp 사용x

n = int(input())

def findMin(num) :
    seven_list = [8,10,18,200,20,28,68]
    if num == 2 :
        return 1
    elif num == 3 :
        return 7
    elif num == 4 :
        return 4
    elif num == 5 :
        return 2
    elif num == 6 :
        return 6
    elif num == 7 :
        return 8
    elif num == 8 :
        return 10
    elif num == 9 :
        return 18
    elif num == 10 :
        return 22
    elif num == 11 :
        return 20
    elif num == 17 :
        return 200
    else :
        idx = num % 7
        cnt = num // 7 - 1
        if idx == 3 :
            return str(seven_list[idx]) + ((cnt-1) * '8')
        else :
            return str(seven_list[idx]) + (cnt * '8')

for _ in range(n) :
    m = int(input())
    r = (m // 7) + 1
    if m % 2 == 0 :
        a_cnt = m // 2
        max_val = '1' * a_cnt
    else :
        b_cnt = m// 2 - 1
        max_val = '7'+'1'*b_cnt
    print(findMin(m), max_val)


