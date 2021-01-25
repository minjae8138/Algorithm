n = int(input())
arr = [ input().upper() for i in range(n) ]
for a in arr :
    if a == a[::-1] :
        print("YES")
    else : print("NO")
    

