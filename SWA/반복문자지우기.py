# 내가 푼 코드
# n = int(input())
# for T in range(1,n+1) :
#     arr = list(input())
#     while True :
#         cnt = 0
#         for i in range(len(arr)) :
#             if arr[i:i+1] == arr[i+1:i+2] :
#                 del arr[i]
#                 del arr[i]
#                 cnt += 1
#                 break
#         if cnt == 0 :
#             break
#     print(f"#{T} {len(arr)}")

# 스텍을 잘 활용한 경우
TC = int(input())
for tc in range(1, TC+1):
    Data = list(input())
    N = len(Data)
    stack = []
    for i in range(N):
        #stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우 
        #=> stack에 저장(append)
        if not stack or stack[-1] != Data[i]:
            stack.append(Data[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우 
        #=> stack에서 제거(pop)
        elif stack and stack[-1] == Data[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')
