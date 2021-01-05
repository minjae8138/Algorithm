n = int(input())
score = list(map(int,input().split()))

# round는 round-half-even 방식이기에 우리가 아는 반올림과는 다르다
# ex) round(4.5) = 4  --> 이처럼 경계값에 있을때 짝수인 방향으로 값을 반환한다
ave = (sum(score)/n) + 0.5
ave = int(ave)
near = float("inf") # 무한대의 숫자 저장, 임의의 큰 수로 대체해도 무방
# 최솟값 구하는 로직
for i in range(len(score)) :
    if abs(score[i] - ave) < near :
        near = abs(score[i] - ave)
        cnt = i
    # 차이값이 같을 경우 처리
    if abs(score[i] - ave) == near :
        if score[i] > score[cnt] :
            cnt = i
        elif score[i] < score[cnt] :
            cnt = cnt
print(ave,cnt+1,end=" ")

