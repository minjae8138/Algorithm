# 처음 푼 풀이 -> 코드가 길어짐

from itertools import combinations

n = int(input())
arr = list(map(int,input().split()))
sum_arr = sum(arr)

# 모든 조합을 all에 담기
all = []
for i in range(1,len(arr)+1) :
    all.append(list(combinations(arr,i)))

# 각각을 리스트로 com_list에 담기
com_list = []
for a in all :
    for val in a :
        com_list.append(val)

# 각 조합의 합을 answer에 담기
answer = []
for c in com_list :
    c= sum(c)
    answer.append(c)

# arr의 합에서 각 조합의 합을 뺀 값이 해당 조합의 합이랑 같으면 YES
# 즉, 조합의 합 중에 sum_arr의 절반에 해당하는 경우가 있으면 YES

res = "NO"
for a in answer :
    if a*2 == sum_arr :
        res = "YES"
        break
print(res)


# dfs로 풀어보기 -> 백트래킹을 활용한 효율적 풀이

def dfs(idx,sum_) :
    global res
    if sum_ > total//2 :  # cut_edge
        return
    if idx == n :
        if sum_ == total-sum_ :
            res="YES"
            return
    else :
        dfs(idx+1, sum_+arr[idx])
        dfs(idx + 1, sum_)

n = int(input())
arr = list(map(int,input().split()))
total = sum(arr)
res = "NO"
dfs(0,0)
print(res)
