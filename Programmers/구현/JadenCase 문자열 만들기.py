def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0 and not s[i].isnumeric() and s[0] != " ":
            t = s[i].upper()
        elif s[i - 1] == " " and not s[i].isnumeric() and s[0] != " ":
            t = s[i].upper()
        else:
            if s[i].isalpha():
                t = s[i].lower()
            else:
                t = s[i]
        answer += t

    return answer

# 파이썬 내장함수 capitalize()를 활용한 색다른 풀이
# capitalize() 자체가 문제에서 요구하는 기능과 동일한 기능을 포함하고 있음 -> 공백 기준으로 첫문자는 대문자로, 나머진 소문자로 변환

    def solution(s):
        return ' '.join([word.capitalize() for word in s.split(" ")])