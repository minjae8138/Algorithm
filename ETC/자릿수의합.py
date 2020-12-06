n= int(input())
lst = list(map(str,input().split()))
print(lst)
## 정석풀이
# 자릿수의 합을 더해주는 함수 작성
def digit_sum(x) :
    sum = 0
    for i in str(x) :
        sum += int(i)
    return sum
# 2^-31과 근접한 값을 max로 둠(0이나 다른 숫자가 들어가도 됨)
max = -2147000000
for i in lst :
    tot = digit_sum(i)
    if tot > max :
        max = tot
        answer = i
print(answer)


# 내가 처음 푼 코드
# def digit_sum(x) :
#     answer = 0
#     sum_list = []
#     for i in lst :
#         cnt = 0
#         for j in range(len(i)) :
#             cnt += int(i[j])
#         sum_list.append(cnt)
#     print(sum_list)
#     for i in range(len(sum_list)) :
#         if sum_list[i] == max(sum_list) :
#             return int(lst[i])
# print(digit_sum(n))