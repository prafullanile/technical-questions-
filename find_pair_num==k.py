arr=[1,2,3,4,3,7,-1]
k=6
seen=set()

for num in arr:
	diff=k-num
	if num in seen:
		print(diff,num)
	seen.add(num)