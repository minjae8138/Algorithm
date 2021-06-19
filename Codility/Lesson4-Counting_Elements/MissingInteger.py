def solution(A):
    A = sorted(A)  # 순서대로 정렬 후 for문을 위함

    # 정렬 한 후 마지막 값이 1보다 작은 경우는 무조건 1
    if A[-1] < 1:
        return 1

    p = 0  # 중복되어 있는 경우는 바로 넘기기 위함
    for i in A:
        if i < 1 or p == i:
            continue

        # 배열 A가 연속적인 숫자로 이루어지지 않은 경우 바로 멈추고 return
        if p + 2 <= i:
            p = p + 1
            break

        # 배열 A가 중간에 멈추지 않고 끝까지 간 경우 마지막 숫자 +1
        if A[-1] == i:
            p = i + 1
            break
        p = i

    return p