# 진법변환
n,b = map(str,input().split())
b = int(b)
answer = 0
cnt = 0
for i in n[::-1] :
    if i.isdigit() : # 숫자인지 아닌지 판별할 때 사용
        val = int(i)
    else:
        val = ord(i)-55 # ord, chr 함수 범위 까먹으면 직접 찍어보기
    answer += b**cnt*val
    cnt+=1
print(answer)

# isdigit,ord 함수는 알고 있는데 잘 활용을 못하는 것 같다
# 비슷한 문제를 풀어보며 몸에 익혀야할듯 
