def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1

    # 길이가 1이 아닌 경우 모든 경우를 다 따져본다
    # result에 모든 갯수 단위에 대한 결과의 길이값들을 담는다
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        for i in range(cut, len(s), cut):  # cut부터 시작해서 cut만큼의 간격으로 이동하는 i
            if s[i:i + cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempStr  # 마지막 값 비교 작업 결과 추가 , 첫번째 케이스의 1개 단위 결과 -> 3c 추가
        length.append(len(result))
        result = ""

    return min(length)