def solution(lottos, win_nums):
    answer = []

    def count(cnt):
        if cnt == 6:
            return 1
        elif cnt == 5:
            return 2
        elif cnt == 4:
            return 3
        elif cnt == 3:
            return 4
        elif cnt == 2:
            return 5
        else:
            return 6

    cnt = 0
    z_cnt = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            z_cnt += 1

    answer = [count(cnt + z_cnt), count(cnt)]
    return answer