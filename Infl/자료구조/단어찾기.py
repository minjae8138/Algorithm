n = int(input())
note = [input() for _ in range(n)]
poem = [input() for _ in range(n-1)]

for a in note :
    if a not in poem :
        print(a)

# dictionary로 풀기(hash)

n = int(input())

poem = dict()
for i in range(n) :
    word = input()
    poem[word] = 1
# 모든 단어에 value로 1을 준다

for i in range(n-1) :
    word = input()
    poem[word] = 0
# 시에 쓰인 단어에 value로 0을 준다

# value가 0인 값을 찾아서 출력
for key, value in poem.items() :
    if value == 1 :
        print(key)
        break