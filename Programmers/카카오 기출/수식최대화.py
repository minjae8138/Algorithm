def solution(expression):
    answer = 0

    # 숫자와 연산자 분리 작업
    ex_list = []  # 숫자,연산자
    numbers = []  # 숫자만
    formula = []  # 연산자만
    a = 0
    for i in range(len(expression)):
        if expression[i] == "-" or expression[i] == "+" or expression[i] == "*":
            numbers.append(int(expression[a:i]))
            formula.append(expression[i])
            ex_list.append(expression[a:i])
            ex_list.append(expression[i])
            a = i + 1
    ex_list.append(expression[a:])
    numbers.append(int(expression[a:]))

    # 연산자 조합 리스트에 담기
    m = 3
    cal_list = ["*", "+", "-"]
    res = [0] * m
    ch = [0] * (m + 1)
    tot_cal = []  # 연산자 조합이 담길 리스트

    def dfs(l):
        if l == m:
            a = ""
            for i in range(m):
                a += res[i]
            tot_cal.append(a)
        else:
            for i in range(m):
                if ch[i] == 0:
                    ch[i] = 1
                    res[l] = cal_list[i]
                    dfs(l + 1)
                    ch[i] = 0
    dfs(0)

    # 연산함수
    def calc(a, b, cal):
        if cal == "*":
            return a * b
        elif cal == "+":
            return a + b
        else:
            return a - b

    # print(numbers)
    # print(formula)

    # 모든 연산자 조합에 대해서 계산하고 temp_numbers에 업데이트
    for cal in tot_cal:
        temp_numbers = numbers[:]
        temp_formula = formula[:]

        for c in cal:
            i = 0
            while (i < len(temp_formula)):
                if temp_formula[i] == c:
                    a = int(temp_numbers[i])
                    b = int(temp_numbers.pop(i + 1))
                    temp_numbers[i] = calc(a, b, c)
                    temp_formula.pop(i)
                    i -= 1
                i += 1

        # 최댓값 찾기
        if abs(int(temp_numbers[0])) > answer:
            answer = abs(int(temp_numbers[0]))
    return answer



# # 정규식을 활용한 짧은 코드
# # expression = "50*6-3*2"
# # expression ="100-200*300-500+20"
#
#
# from itertools import permutations
# import re
#
#
# def solution(expression):
#     expressions = set(re.findall("\D", expression))  # expression에 있는 연산자 추출
#     prior = permutations(expressions)
#     cand = []
#
#     for op_cand in prior:
#         temp = re.compile("(\D)").split('' + expression)  # 연산자와 숫자 구분
#         for exp in op_cand:
#             while exp in temp:  # temp에 해당 연산자가 없을때까지 진행
#                 idx = temp.index(exp)
#
#                 # 해당 연산자 앞뒤로 계산한 것을 중앙에 두고 왼쪽 오른쪽에 있는 값들 붙이기
#                 temp = temp[:idx - 1] + [str(eval(''.join(temp[idx - 1:idx + 2])))] + temp[idx + 2:]
#         cand.append(abs(int(temp[0])))
#     return max(cand)
#
# # solution(expression)



