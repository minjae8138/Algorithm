def solution(n):
    return len([i  for i in range(1,n+1,2) if n % i == 0])

# a + (a+1) + (a+2) + ... + (a+k-1) = k(2a+k-1)/2 = n
# k(2a+k-1)/2 = n을 a에 대해서 정리하면 a = n/k + (1-k)/2
# 따라서 k는 n의 약수이고 (1-k)가 2의 배수여야하므로 k는 홀수임을 알 수 있다