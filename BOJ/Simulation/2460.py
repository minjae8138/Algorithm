cnt = 0
lst = []
for _ in range(10) :
    a,b = map(int,input().split())
    cnt -= a
    cnt += b
    lst.append(cnt)
print(max(lst))