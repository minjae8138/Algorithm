def solution(genres, plays):
    answer = []
    dic = {}
    total = []
    # dic 생성 => 장르별 총 재생수를 나타내는 dictionary
    # total 생성 => genres + plays
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        total.append([genres[i], plays[i]])

    # s_dic => dic을 리스트로 형식으로 변경
    s_dic = []
    for key, value in dic.items():
        s_dic.append([key, value])
    s_dic = sorted(s_dic, key=lambda x: x[1], reverse=True)

    # total에 idx 정보 추가
    # 기존 total = [["classic", 500],["pop", 300]]
    # idx 추가 후 total = [["classic", 500, 0],["pop", 300, 1]]
    for i in range(len(total)):
        total[i] = total[i] + [i]

    # s_total => total을 재생수(total[1])에 따른 내림차순으로 정렬
    s_total = sorted(total, key=lambda x: x[1], reverse=True)

    for i in range(len(s_dic)):  # 장르 갯수만큼 회전

        cnt = 0  # 장르당 최대갯수가 2개이기에 cnt를 설정하여 컨트롤
        for t in s_total:
            if cnt > 2:
                break
            if t[0] == s_dic[i][0]:
                cnt += 1
                if cnt > 2:
                    break
                answer.append(t[2])

    return answer


# 다른 사람 풀이
# dic을 두 개로 두어 직관적이고 효율적으로 풀음
# zip 활용과 dictionary를 정렬한 코드가 인상적임

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    # zip과 enumerate를 통해 한 번에 처리
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    # dictionary의 이중포문을 통해 한 방에 인덱스 리스트 추출
    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        print(k, v)
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:  # 최대 2개 조건을 슬라이싱으로 해결
            answer.append(i)

    return answer