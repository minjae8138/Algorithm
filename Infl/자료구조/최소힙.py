import heapq
num = -100
arr = []
while num != -1:
    num = int(input())
    if num == 0:
        if arr == [] :
            print(-1)
        else :
            print(heapq.heappop(arr))
    elif num > 0 :
        heapq.heappush(arr,num)

