# 키로거
# 기존의 스택을 사용한 코드는 시간초과
# 연결리스트로 해결해야함


from sys import stdin
for _ in range(int(stdin.readline())):
    typing = stdin.readline().strip()
    left, right = [], [] # 커서 기준 왼쪽 오른쪽 리스트 배치
    for typ in typing:
        if typ == '<':
            if left:
                right.append(left.pop())
        elif typ == '>':
            if right:
                left.append(right.pop())
        elif typ == '-':
            if left:
                left.pop()
        else:
            left.append(typ)
    left.extend(reversed(right)) # 오른쪽에 남아있는 문자가 있으면 역순으로 합치기

    print(''.join(left))


# 내 풀이 - 시간초과
# from sys import stdin
# for _ in range(int(stdin.readline())):
#     arr = stdin.readline().strip()
#     string = []
#     keyb = 0
#     for a in arr :
#         if keyb != 0 and a == "<" :
#             keyb -= 1
#             continue
#         elif keyb < len(string) and a ==">" :
#             keyb += 1
#             continue
#         elif string and a == "-" :
#             string.pop()
#             continue
#         elif a ==">" or a=="<" or a=="-" :
#             continue
#         else :
#             string.insert(keyb,a)
#             keyb += 1
#     print(''.join(string))
