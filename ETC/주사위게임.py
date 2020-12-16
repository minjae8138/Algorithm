import collections
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
lst = []
res = 0
for a in arr :
    k = 0
    for i in range(3) :
        if collections.Counter(a)[a[i]] == 3 :
            k = 10000 + a[i] * 1000
            
        elif collections.Counter(a)[a[i]] == 2 :
            k = 1000 + a[i] * 100
            
        else :
            k = max(a) * 100
            
        if k > res :
            res = k
print(res)