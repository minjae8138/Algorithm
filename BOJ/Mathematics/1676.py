# 일반적인 재귀나 for문으로는 시간복잡도가 너무 커진다
# 5의 갯수만큼 0이 붙는다는 것에 착안한 풀이


n = int(input())
total = 0
i = 5

# 5^n 이면 5가 여러 개이므로 5의 배수마다 반복작업 필요
while i<=n :
    total += n//i
    i *= 5
print(total)