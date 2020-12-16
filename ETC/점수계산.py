n = int(input())
arr = list(map(int,input().split()))

max = 0
cnt = 0
for a in arr :
    if a == 1 :
        max += 1
        cnt += max
    elif a == 0 :
        max = 0
print(cnt)