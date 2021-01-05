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

# from collections import deque

# T = int(input())

# for test_case in range(1,T+1):
#     n,m = map(int, input().split()) # 화덕 n, 피자 m
#     pizza = deque([(i+1,j) for i,j in enumerate(list(map(int, input().split())))])
#     c = deque()

#     for i in range(n):
#         c.append(pizza.popleft())

#     while len(c) > 1:
#         p = c.popleft()
#         cheeze = p[1]//2
#         if cheeze == 0 and pizza:
#             c.append(pizza.popleft())
#         elif cheeze == 0 and not pizza:
#             continue
#         else:
#             p = (p[0],p[1]//2)
#             c.append(p)
#     print(f'#{test_case}',c[0][0]) 
    

