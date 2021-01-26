# 다시 풀어서 해결함
a,b = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
val = []
for i in range(len(arr)) :
    val.append(arr[i])
    if sum(val) == b :
        # print("같을 때 - ",i,val)
        cnt += 1
        val = [arr[i]]
    elif sum(val) < b :
        # print("작을 떄 - ",i,val)
        continue
    elif sum(val) > b :
        # print("클 때 - ", i,val)
        while sum(val) > b :
            if arr[i] == b:
                # print("해당 인덱스일때 - ", i, val)
                cnt += 1
                val = []
                break
            val.pop(0)
            if sum(val) == b :
                cnt+=1
                val=[val[-1]]
                # print("같은 값 발견 - ",i,val)
                break
            elif sum(val) < b :
                val = [val[-1]]
print(cnt)
# 다시 풀어보니까 여러 번의 코드 수정은 있었지만, 큰 막힘없이 스스로 풀 수 있었다
# 에러나 오답일 경우 원인을 차근차근 파악하며 해결해나가다 보니 풀게 되었다


# 다른 정답코드
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


