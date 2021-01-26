n = int(input())
matrix = [list(map(int,input().split())) for i in range(n)]
# print(matrix)

lst = []
lt = rt = mid = n//2
for i in range(mid+1) :
    lst.append(sum(matrix[i][lt:rt+1]))
    if lt > 0 :
        lt-=1
        rt+=1
for i in range(mid+1,n) :
    lt += 1
    rt -= 1
    lst.append(sum(matrix[i][lt:rt+1]))

print(sum(lst))