def solution(citations):
    num = len(citations)
    while True :
        cnt = 0
        for i in citations :
            if i >= num :
                cnt +=1
        if cnt >= num :
            return num
        else :
            num -= 1