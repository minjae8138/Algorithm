def solution(ph):
    ph.sort()
    for i in range(len(ph)-1) :
        cur = len(ph[i])
        if ph[i] == ph[i+1][:cur] :
            return False
    return True

# 다른 사람 풀이
# zip과 startswith 활용한 코드
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True