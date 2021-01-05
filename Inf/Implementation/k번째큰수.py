from itertools import combinations
n,k = map(int,input().split())
lst = list(map(int,input().split()))
lst = set(lst) 
comb = list(combinations(lst,3))

#list(map(함수,변수)), 여기서는 lambda가 함수
comb_sum = sorted(list(map(lambda x : x[0] + x[1] + x[2], comb)),reverse = True)
print(comb_sum[k-1])

# 3중 for문으로도 풀 수 있지만, combinations 함수와 lambda로 푸는 것이 핵심

## 3중 for문 식
# n,k = map(int,input().split())
# lst = list(map(int,input().split()))
# res = set() --> 이렇게 하면 res에는 자동 중복 처리 
# for i in range(n) :
#     for j in range(i+1,n) :
#         for m in range(j+1,n) :
#             res.add(lst[i] + lst[j] + lst[m] --> set자료형에는 add함수를 사용해 추가
# res = list(res)
# res.sort(reverse = True)
# print(res[k-1])
