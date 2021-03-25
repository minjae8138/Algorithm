# n = int(input())
#
# answer = []
# def dfs(n) :
#     r = n % 2
#     if n <=1 :
#         answer.append(r)
#         for a in answer[::-1]:
#             print(a, end="")
#         return
#
#     answer.append(r)
#     # print(r,end="")
#     n = n//2
#
#     return dfs(n)
#
# dfs(n)

n=int(input())

print(bin(n)[2:])


