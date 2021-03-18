import sys
n = int(sys.stdin.readline())

arr = [list(map(int,input().split())) for _ in range(n)]
arr = sorted(arr,key = lambda x: (x[1], x[0])) # -> 핵심 코드
                                               # -> 끝나는 시간으로 내림차순 후 시작 시간으로 오름차순 정렬

cur = arr[0][1]
large = 1
for i in range(1,n) :
    if arr[i][0] >= cur  :
        large += 1
        cur = arr[i][1]
print(large)