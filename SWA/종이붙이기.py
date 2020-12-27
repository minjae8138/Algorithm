arr = [0] * 31
def dp(x) :
    if x == 1 :
        return 1
    if x == 2 :
        return 3
    if x == 3 :
        return 5
    if x >= 4 :
        arr[x] = dp(x-1) + 2*dp(x-2)
    return arr[x]
number = 0
t = int(input())
for _ in range(t) :
    n = int(input())//10
    number += 1
    print(f"#{number} {dp(n)}")