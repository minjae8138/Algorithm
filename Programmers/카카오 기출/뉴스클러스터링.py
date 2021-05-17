import re


def solution(str1, str2):
    answer = 0

    # 대문자로 통일
    str1 = str1.upper()
    str2 = str2.upper()

    # 두 개 단위로 나누기
    str1_list = []
    str2_list = []
    for i in range(1, len(str1)):
        a = re.findall(r'[^a-zA-Z]', str1[i - 1])
        b = re.findall(r'[^a-zA-Z]', str1[i])

        if str1[i - 1] == " " or str1[i] == " ":
            pass
        elif a or b:
            pass
        else:
            two_str = str1[i - 1] + str1[i]
            str1_list.append(two_str)
    for i in range(1, len(str2)):
        a = re.findall(r'[^a-zA-Z]', str2[i - 1])
        b = re.findall(r'[^a-zA-Z]', str2[i])

        if str2[i - 1] == " " or str2[i] == " ":
            pass
        elif a or b:
            pass
        else:
            two_str = str2[i - 1] + str2[i]
            str2_list.append(two_str)

    # 교집합
    common = []  # 공통되는 값 뽑기
    for s in set(str1_list):
        if s in set(str2_list):
            common.append(s)

    result1 = []
    result2 = []
    for c in common:
        # 교집합에 쓰일 최솟값
        min_val = min(str1_list.count(c), str2_list.count(c))
        result1.append(min_val)
        # 합집합에 쓰일 최댓값
        max_val = max(str1_list.count(c), str2_list.count(c))
        result2.append(max_val)

    # 합집합
    new1 = []
    new2 = []
    for i in range(len(str1_list)):
        if str1_list[i] not in common:
            new1.append(str1_list[i])
    for i in range(len(str2_list)):
        if str2_list[i] not in common:
            new2.append(str2_list[i])

    common_val = sum(result1)
    sum_val = len(new1) + len(new2) + sum(result2)
    if sum_val == 0:

        return 65536
    else:
        answer = (common_val / sum_val) * 65536

        return int(answer)