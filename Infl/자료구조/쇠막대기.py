arr = list(map(str,input()))
# print(arr)

stack = []
sum = 0
for i in range(len(arr)) :
    if arr[i] == "(" :
        stack.append(arr[i])
    elif arr[i] == ")" and arr[i-1] == "(" :
        stack.pop()
        sum += len(stack)
    elif arr[i] == ")" and arr[i-1] != "(" :
        stack.pop()
        sum += 1
print(sum)