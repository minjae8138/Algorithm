# # 처음 풀이 - 시간초과
# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# start = 0
# end = 1
# cnt = 0
# while True  :
#     if sum(arr[start:end]) == m :
#         cnt += 1
#         start += 1
#         end = start + 1
#     elif sum(arr[start:end]) < m :
#         end += 1
#     elif sum(arr[start:end]) > m :
#         start += 1
#         end = start + 1
#     if start == n-1 :
#         break
# print(cnt)

##다시풀기

n,m = map(int,input().split())
arr = list(map(int,input().split()))
lt = 0
rt = 1
tot = arr[0]
cnt = 0
while True:
    if tot<m:
        if rt<n:
            tot+=arr[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=arr[lt]
        lt+=1
    else:
        tot-=arr[lt]
        lt+=1
print(cnt)


        


