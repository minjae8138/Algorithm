# 7이하의 트리(전위, 중위, 후위) -> 출력의 위치만 바꿔주면 된다

# 전위순회(깊이우선)
def dfs(v) :
    if v > 7 :
        return
    else :
        print(v)
        dfs(2*v)
        dfs(2*v+1)
dfs(1)

# 중위순회
def dfs(v) :
    if v > 7 :
        return
    else :
        dfs(2*v)
        print(v)
        dfs(2*v+1)
dfs(1)

# 후위순회(너비우선)
def dfs(v) :
    if v > 7 :
        return
    else :
        dfs(2*v)
        dfs(2*v+1)
        print(v)
dfs(1)