n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
lst = []

for a in arr :
    lst.append(sum(a))
for i in range(n) :
    row = 0
    for j in range(n) :
        row += arr[j][i]
    lst.append(row)
#왼쪽대각선
left = 0
for i in range(n) :
    left+=arr[i][i]
lst.append(left)
#오른쪽대각선
right = 0
a = 0
b = n-1
while a<n :
    right+=arr[a][b]
    a+=1
    b-=1
lst.append(right)
print(max(lst))

#대각선 한번에 구현하는 코드
# left = right = 0
# for i in range(n) :
#     left += arr[i][i]
#     right += arr[i][n-1-i]
# lst.append()
# --> a,b값 설정안하고도 right를 구한것이 핵심