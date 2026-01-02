# Write a program to merge two lists and remove duplicates

list1 = [1, 12, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list(set(list1 + list2))
print(merged)

# merged without change order
list1 = [1, 9, 3, 4, 5]
list2 = [4, 5, 12, 7, 8]

merge = []
for item in list1 + list2:

	if item not in merge:
		merge.append(item)

print(merge)