import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

def next_permutation(lst):
    if len(lst) == 1:
        return [-1]
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] > lst[i - 1]:
            break
    if i == 1 and lst[0] > lst[1]:
        return [-1]
    # i - 1 인덱스하고 i ~ len(lst) - 1 인덱스에서
    # i-1 인덱스값보다 크면서 제일 작은거랑 바꿔야함
    # 끝에는 내림차순이기에 끝에서부터 비교 ㄱㄱ
    for j in range(len(lst) - 1, -1, -1):
        if lst[j] > lst[i - 1]:
            break
    # 이제 j 인덱스랑 i - 1인덱스랑 바꿔주면 됨
    tmp = lst[j]
    lst[j] = lst[i - 1]
    lst[i - 1] = tmp
    # 성주가 바뀌었으니 새마음 새출발 끝 원소들 오름차순 정리
    lst = lst[:i] + sorted(lst[i:])
    return lst

print(' '.join(map(str, next_permutation(lst))))

for i in range(5) :
    if i> 3 :
        break
print(i)