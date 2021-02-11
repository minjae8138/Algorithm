# 이분탐색 코드
n,m = map(int,input().split())
lst = list(map(int,input().split()))

lt,rt = 0, n-1
lst.sort()
mid = 0
while lst[mid] != m :
    mid = (lt+rt)//2
    if lst[mid] > m :
        rt = mid-1
    elif lst[mid] < m :
        lt = mid+1
print(mid+1)

# 인덱스 활용한 코드
## 이 문제는 이분탐색을 사용하지 않고 간단하게 풀 수 있긴함
b = sorted(lst).index(m)+1 # 인덱스를 사용하면 한줄로 해결 // 하지만 이분탐색 코드에도 익숙해져야 한다
print(b)



