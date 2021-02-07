def solution(s, n):
    answer = ''
    # ord를 사용할 땐 보통 ord('a')나 ord('A')를 빼주어 연산한다
    for i in s :
        if i.isupper() :
            answer += chr(((ord(i)-ord('A')+n)%26) +ord('A'))
        elif i.islower() :
            answer += chr(((ord(i)-ord('a')+n)%26) +ord('a'))
        else :
            answer += i
    return answer