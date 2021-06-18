N,M = map(int,input().split())

day = 0
while N != 0 :
	day += 1
	if day % M == 0 :
		N+=1
	N-=1
print(day)