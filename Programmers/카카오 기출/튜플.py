def solution(s):
    answer = []
    # 리스트로 변환
    s = s[2:-2]
    s = s.split("},{")

    # 길이로 정렬
    l = sorted(s, key=lambda x: len(x))

    # 원소를 리스트 형식으로 변환하여 new에 저장
    new = []
    for i in l:
        new.append(i.split(","))

    # answer에 없으면 추가 (중복제거 로직과 동일)
    for i in new:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


# #  Counter 함수를 응용한 풀이법
# import re
# from collections import Counter
#
# def solution(s):
#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

