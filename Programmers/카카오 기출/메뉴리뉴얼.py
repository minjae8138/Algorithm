# Counter와 most_common 활용법에 대해 알게 되었음
# Counter로 받고 (A,B) 형식에서 for 문을 통해 A,B를 변수로 받는 것이 유용했음(여기선 메뉴와 카운트)

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        candidate = []
        for order in orders:
            for comb in combinations(order, c):
                res = ''.join(sorted(comb))
                candidate.append(res)

        sorted_candidate = Counter(candidate).most_common()
        answer += [menu for menu, cnt in sorted_candidate if cnt > 1 and cnt == sorted_candidate[0][1]]
        # sorted_candidate[0][1] 는 가장 주문이 많은 메뉴의 주문횟수(most_common에 의해 가장 앞에 있는 것이 횟수가 가장 많은 메뉴임)
        # 따라서 cnt == sorted_candidate[0][1]  이 부분은 가장 많은 횟수에 해당하는 메뉴를 필터링해주는 코드

    return sorted(answer)