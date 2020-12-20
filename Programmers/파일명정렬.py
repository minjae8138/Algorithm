def solution(files):
    answer = []
    # 빈 문자열일 때 index error 나기때문에 맨뒤에 공백추가 ex) "F-15"
    files = list(map(lambda x : x + " ",files))
    
    # idx는 head와 num이 같을 경우 index순서대로 정렬해야되서 필요
    for idx, f in enumerate(files) :
        parts=[]
        temp = 0
        for i in range(len(f)) :
            if not f[i].isnumeric() and f[i+1].isnumeric():
                parts.append(f[:i+1]) # head부분
                temp = i + 1
            elif f[i].isnumeric() and not f[i+1].isnumeric() :
                parts.append(f[temp:i+1]) # num 부분
                parts.append(f[i+1:]) # tail 부분
                parts.append(idx)
                break # 중간에 break가 되어 f[:i+1] 코드가 index error가 안남
        answer.append(parts)
    answer = sorted(answer, key = lambda x :[x[0].lower(), int(x[1]), x[3]])
    return list(map(lambda x : "".join(x[:-1]).strip(), answer))