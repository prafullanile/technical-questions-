arr=[2,4,3,2,5,7,1]

smallest=arr[0]

for i in arr:

	if i <  smallest:

		smallest=i
print(smallest)

#with min method
print(min(arr))