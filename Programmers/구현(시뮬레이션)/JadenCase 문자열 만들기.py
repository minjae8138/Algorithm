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
