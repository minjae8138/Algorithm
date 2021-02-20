n,c = map(int,input().split())
horse = [int(input()) for _ in range(n)]
horse.sort()
lt = 1
rt = horse[-1]
res = 0
while lt <= rt :
    mid = (lt+rt) // 2
    lst = [horse[0]]
    for i in range(1,len(horse)) :
        if horse[i] - lst[-1] >= mid :
            lst.append(horse[i])
    if len(lst) >=c :
        res = mid
        lt = mid+1
    else :
        rt = mid - 1

print(res)

