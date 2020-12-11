n = int(input())
lst = list(map(int,input().split()))
bin = []
def eros(x) :
    for i in range(2,x) :
        if x % i == 0 :
            return False
    return True

for i in range(len(lst)) :
    lst[i] = int(str(lst[i])[::-1])
    if eros(lst[i]) :
        print(lst[i],end=" ")
# lst[::-1] --> 유용한 코드이니까 숙지하기

## 함수를 만들어서 뒤집는 방법
# def reverse(x) :
#     res = 0
#     while x > 0 :
#         t = x % 10
#         res = res*10 + t
#         x = x//10
#     return res


