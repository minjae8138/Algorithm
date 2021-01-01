n = input()
# 30의 배수는 3의 배수 & 10의 배수
sum_n = 0
for i in n :
    sum_n += int(i)
# 3의 배수일때랑 10의 배수일 때 처리코드
if sum_n % 3 == 0 & n.count('0') > 0 :
    answer = sorted(n,reverse=True) # 큰 숫자부터 출력하면 자동적으로 0이 맨 뒤로 보내짐
    answer = ''.join(answer)
else :
    answer = -1
print(answer)