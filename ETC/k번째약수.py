n = int(input())
k = int(input())
lst = []
def sol(n,k) :
  for i in range(1,n+1) :
    if n % i == 0 :
      lst.append(i)
  if lst == [] or k >= len(lst) :
    return -1
  return lst[k-1]