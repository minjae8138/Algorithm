arr,m = map(int,input().split())
arr = list(map(int,str(arr)))
stack = []
for a in arr :
    while stack and m>0 and stack[-1] < a :
        stack.pop()
        m -= 1
    stack.append(a)
if m > 0 :
    stack = stack[:-m]
print(''.join(map(str,stack)))

        

