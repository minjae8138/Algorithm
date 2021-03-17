import heapq

arr = []
while True :
    num = int(input())
    if num == -1 :
        break
    elif num == 0 :
        if arr == [] :
            print(-1)
        else :
            print(-heapq.heappop(arr))

    elif num > 0 :
        heapq.heappush(arr,-num)