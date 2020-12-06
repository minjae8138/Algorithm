T = int(input())
for i in range(T) :
    N, s,e,k = map(int,input().split())
    lst = list(map(int,input().split()))

    select_lst = sorted(lst[s-1:e])
    print(select_lst[k-1])