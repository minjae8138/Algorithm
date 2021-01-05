n = int(input())
arr = [ str(input()) for i in range(n) ]
for a in arr :
    if a.upper() == a[::-1].upper() :
        print("YES")
    else : print("NO")
    

