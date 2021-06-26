def solution(numbers):
    sort_num = sorted(list(map(str, numbers)), key=lambda x: x * 3, reverse=True)
    return str(int("".join(sort_num)))      # [0,0,0] -> "0" 처럼 0으로 이루어진 케이스 때문에 int를 거쳐서 str로 변환해야함