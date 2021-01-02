# 진법변환2
n,b = map(int,input().split())
lst = []
while n > 0 :
    r = n % b
    n = n// b
    lst.append(r)
for i in lst[::-1] : # sorted(reverse=True)와 헷갈리지 않기
    if i < 10 :
        val = i
    else :
        val = chr(i+55) # 처음에 chr(i) +55 로 해서 오류났었음, ord의 경우에는 인수가 str이지만 chr의 경우가 인수가 int이기에 chr(i+55)가 맞다
    print(val,end='')