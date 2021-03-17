# 내 풀이 - 딕셔너리 (해쉬)

ana = dict()
stack = []

for word in input() :
    if word in stack :
        ana[word] += 1
    else :
        ana[word] = 1
        stack.append(word)

for word in input() :
    if word in stack :
        ana[word] -= 1

answer = "YES"
for key, value in ana.items() :
    if value != 0 :
        answer = "NO"
        break
print(answer)

# 풀이 2 - 딕셔너리의 get 함수 활용하기기

ana = dict()

for word in input() :
    ana[word] = ana.get(word,0) + 1   # ana에서 word에 해당하는 value를 반환, word값이 없으면 0 반환

for word in input() :
    ana[word] = ana.get(word,0) - 1

if sum(ana.values()) == 0 :
    print("YES")
else :
    print("NO")