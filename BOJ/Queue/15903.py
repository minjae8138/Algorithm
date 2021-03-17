# 처음 푼 풀이
n,m = map(int,input().split())
cards = list(map(int,input().split()))

for _ in range(m) :
    cards.sort()
    change = cards[0] + cards[1]
    cards[0] = change
    cards[1] = change

print(sum(cards))

# heapq 풀이
# --> 메모리는 살짝 더 사용하고 시간이 반 이상 줄어든다
n,m = map(int,input().split())
cards = list(map(int,input().split()))

import heapq
heapq.heapify(cards)

for _ in range(m) :
    a = heapq.heappop(cards) + (heapq.heappop(cards))
    heapq.heappush(cards,a)
    heapq.heappush(cards,a)

print(sum(cards))