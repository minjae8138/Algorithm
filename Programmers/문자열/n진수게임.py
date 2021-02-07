def solution(n, t, m, p):
    Rota = '0123456789ABCDEF' # 16개의 문자열 저장

    # 진법변환 코드
    def change(x,n) :
        q,r = divmod(x,n)
        k = Rota[r]
        return change(q,n) + k if q else k

    # 0부터 t*m까지의 숫자를 진법변환하여 answer에 담기    
    answer = ''    
    for i in range(t*m+1) : # 사람수*순서만큼 범위지정
        answer+=change(i,n)

    # answer에서 순서(p)에 맞는 값 추출하여 result에 담기
    result=''
    for i in range(len(answer)) :
        if (i+1-p)%m == 0 :
            result+=answer[i]
        if len(result) == t :
            break
    return result