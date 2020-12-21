import collections
n,c = map(int,input().split())
arr = list(map(int,input().split()))
# arr = [1,2,3,4,5,6,6,6,5,4,4,21,21,21,21]
b=collections.Counter(arr)
items_lst = sorted(b.items(),key = lambda x : x[1],reverse = True)
lst = ''
for items in items_lst :
    for i in range(items[1]) :
        print(items[0],end=' ')