t = int(input())
for T in range(1,t+1) :
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f"#{T} {arr[m%n]}")

