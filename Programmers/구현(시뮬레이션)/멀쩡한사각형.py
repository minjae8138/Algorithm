import math
def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

# 대각선이 교점을 지날 때의 작은 사각형은 전체 사각형을 닮는 경우이다
# 즉, 최대 공약수 개념을 적용할 수 있음
# 작은 사각형마다 w+h -1 만큼 지나감, 즉 w+h - w와 h의 최대공약수(작은 사각형 갯수)를 뺀 w+h - math.gcd(w,h) 만큼 지나친다.