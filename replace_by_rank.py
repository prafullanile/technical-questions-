def rank_fun(arr):

	sorted_arr=sorted(set(arr))


	rank_map={val:rank+1 for rank,val in enumerate(sorted_arr)}

	return [rank_map[x] for x in arr]

arr=[20,30,40,10,5]

print(rank_fun(arr))