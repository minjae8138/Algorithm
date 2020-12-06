def solution(people, limit):
    p = sorted(people)
    l = len(p) - 1   
    answer = 0
    start_idx = 0
    end_idx = l
    
    while start_idx < end_idx :
        if p[start_idx] + p[end_idx] <= limit :
            start_idx += 1
            end_idx -= 1
            answer +=1
        else:
            end_idx -=1          
    return len(p) - answer