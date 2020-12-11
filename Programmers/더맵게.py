import heapq
def solution(scv, K): 
    answer = 0 
    heapq.heapify(scv) # 기존의 list를 heap구조에 담기 (자동정렬)

    # heappush(heap,item)
    # heap에 item을 추가
    while scv[0] < K: 
        try: 
            heapq.heappush(scv,heapq.heappop(scv)+(heapq.heappop(scv)*2))  #heappop은 heap에서 최솟값을 삭제하고 반환 
        except IndexError: 
            return -1 
        answer += 1 
    return answer