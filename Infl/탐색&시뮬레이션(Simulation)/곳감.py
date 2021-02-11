n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

natrix = matrix

m = int(input())

# 회전한 매트릭스 구하기
for _ in range(m) :
    row, direct, num = map(int,input().split())
    if direct == 0 :
        for _ in range(num) :
            left = natrix[row-1].pop(0)
            natrix[row-1].append(left)
            # print(natrix[row-1])
    elif direct == 1 :
        for _ in range(num) :
            right = natrix[row-1].pop(-1)
            natrix[row-1].insert(0,right)
            # print(natrix[row-1])
# 다이아몬드 갯수 세기
s = 0
e = n
mid = n//2
answer = 0

for i in range(mid+1) :
    # print(natrix[i][s:e])
    answer += sum(natrix[i][s:e])
    # print(answer)
    s+=1
    e-=1

s = mid
e = mid+1
for i in range(mid+1,n) :
    s -= 1
    e += 1
    # print(natrix[i][s:e])
    answer += sum(natrix[i][s:e])
print(answer)








