n = int(input())
lst = []
for _ in range(n) :
    a,b = map(int,input().split())
    lst.append([a,b])

# 정렬
arr =  sorted(lst,key=lambda x: x[0])

# 빈 곳에 해당 인덱스와 0 채우기
for i in range(arr[-1][0]+1) :
    for j in range(len(arr)) :
        if i == arr[j][0] :
            break
        if i < arr[j][0] :
            arr.insert(j,[i,0])
            break

# 제일 큰 막대 인덱스 구하기
largest = max(lst,key=lambda x:x[1])
max_idx = largest[0]

# 제일 큰 막대 인덱스 기준으로 왼쪽 오른쪽 분리

# 왼쪽
left = arr[:max_idx+1]
sum = 0
large = 0
for i in range(len(left)) :
     if left[i][1] > large :
         large = left[i][1]
     sum += large
# 오른쪽
right = arr[max_idx+1:]
large = 0
for i in range(len(right)-1,-1,-1) :
    if right[i][1] > large :
        large = right[i][1]
    sum += large
print(sum)