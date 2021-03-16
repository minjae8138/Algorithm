topni = [list(map(int,input())) for _ in range(4)]
n = int(input())

for _ in range(n) :
    which, rotate = map(int,input().split())
    a = which + 1   # which값 초기화를 위해 만듦
    b = rotate + 1
    going = [[which-1,rotate]] # 회전할 톱니바퀴 체크해서 담기

    # 기준 톱니바퀴의 왼쪽부분 체크
    while True :
        if which-1 < 1 :
            break
        if topni[which-1][6] != topni[which-2][2] :
            if rotate == 1 :
                going.append([which-2,-1])
                rotate = -1
            else :
                going.append([which-2,1])
                rotate = 1
        else :
            break
        which -= 1
    # which 값 초기화
    which = a - 1
    rotate = b - 1

    # 기준 톱니바퀴의 오른쪽부분 체크
    while True :
        if which > 3 :
            break
        if topni[which][6] != topni[which-1][2] :
            if rotate == 1 :
                going.append([which,-1])
                rotate = -1
            else :
                going.append([which,1])
                rotate = 1
        else :
            break
        which += 1

    # 체크한 톱니바퀴 회전하는 코드
    for w in going :
        cur = topni[w[0]]
        if w[1] == 1 :
            cur = cur.insert(0,cur.pop())
        elif w[1] == -1 :
            cur = cur.append(cur.pop(0))

# print(topni)
num = 1
answer = 0
for i in range(4) :
    answer += topni[i][0] * num
    num *= 2
print(answer)


