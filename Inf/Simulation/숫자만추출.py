n = str(input())
answer = ''
for i in n : 
    try : 
        i = int(i)
        answer += str(i)
    except : continue
answer = int(answer)
cnt = 0
for i in range(1,answer+1) :
    if answer % i == 0 :
        cnt += 1
print(answer)
print(cnt)
