## [0] * (n+1) 리스트를 활용한 풀이
 
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)


## 내가 푼 풀이  --> 효율성이 안 좋음

# n= int(input())
# lst= []
# num= 2
# for k in range(2,n+1) :
#     lst.append(k)
# for i in range(2,n+1) :
#     for j in range(2,n+1) :
#         if i*j in lst :
#             lst.remove(i*j)
# print(len(lst))




    


    