def mod(x) :
    x // 2

t = int(input())
for T in (1,t+1) :
    n,m = map(int,input().split())
    s_arr= list(map(int,input().split()))
    print(s_arr)
    arr = s_arr[n:]
    print(arr)
    que = s_arr[:n]
    print(arr)
    que.sort()
    print(que)
    while len(que) > 1 :
        for i in range(n) :
            que[i] = que[i] // 2
            
            if que[i] == 0 :
                if not arr :
                    add = arr.pop(0)
                    que[i] = add
            if not arr :
                if que[i] == 0 :
                    que.pop()
    print(que)   
    

