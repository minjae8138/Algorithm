arr = [list(map(int,input().split())) for i in range(10)]
lst = []
[lst.append(i) for i in range(21)]

# print(arr)
# print(lst)


for a in arr :
    lst[a[0] : a[1]+1] = lst[a[1] : a[0]-1 : -1]
lst.pop(0)
for i in lst :
    print(i,end=" ")

