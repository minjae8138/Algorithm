N = int(input())

current = N
stack = [N]
while True:
    summed = 0
    for digit in str(current):
        summed += int(digit) ** 2   # 각 자리 제곱합

    if summed not in stack:
        stack.append(summed)        # stack에 summed를 담는다
        current = summed

    # stack에 있는 경우(같은 패턴) UNHAPPY, 1이면 HAPPY
    # 1인 경우 그 다음수도 계속 1이 추가됨
    elif summed == 1:
        print('HAPPY')
        break
    else:
        print('UNHAPPY')
        break


