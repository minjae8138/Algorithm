n,k = map(int,input().split())
arr = list(map(str,input()))
arr.insert(0,0)
lst = [0]*(n+1)
cnt= 0

for i in range(1,len(arr)) :
    if arr[i] == 'P' and i-k > 0:
        for j in range(k,0,-1) :
            if arr[i-j] == 'H' and lst[i-j] == 0 :
                lst[i-j] = 1
                lst[i] = 1
                cnt += 1
                break
            
    elif arr[i] == 'P' and i+k < n+1 :
        for j in range(1,k+1) :   
            if arr[i+j] == 'H' and lst[i+j] == 0 :
                lst[i+j] = 1
                lst[i] = 1
                cnt += 1
                break
            
print(cnt)