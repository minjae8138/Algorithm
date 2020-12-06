import collections
N, M = map(int,input().split())
lst = []
answer = []
for i in range(1,N+1) :
    for j in range(1,M+1) :
        lst.append(i+j)
a = collections.Counter(lst)
# a에서 빈도수가 가장 많은 값 추출
# Counter은 dictionary와 동일하게 처리 가능
# {key1 : value1, key2 : value2, ...}
b = max(list(a.values()))
for i in a :
    if a[i] == b :
        print(i,end=" ")
#------------------------------------
# collection 함수를 사용하지 않을 때 풀이법
# n, m=map(int, input().split())
# [0,0,0,......] 생성
# cnt=[0]*(n+m+3) -> +3 이 아니어도 상관 x
# max=0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j]=cnt[i+j]+1

# for i in range(n+m+1):
#     if cnt[i]>max:
#         max=cnt[i]
    
# for i in range(n+m+1):
#     if cnt[i]==max:
#         print(i, end=' ')