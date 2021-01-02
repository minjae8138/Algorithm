t = int(input())
number = 0
for T in range(1,t+1) :
    n = input()
    lst = []
    cnt = 0
    number +=1
    for i in n :
        if i not in "(){}" :
            continue
        elif i == '(' or i == '{' :
             lst.append(i)
        elif lst and i == ')' and lst[-1] == '(' :
            lst.pop()
        elif lst and i == '}' and lst[-1] == '{' :
            lst.pop()
        else :
            lst.append(i)
    if len(lst) != 0 :
        print(f"#{number} 0")
    else :
        print(f"#{number} 1")