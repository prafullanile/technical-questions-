def long_pol(arr):
	longest = ""

	for item in arr:

		s = str(item)

		if s == s[:: -1]:

			if len(s) > len(longest):
				longest = s

	return longest if longest else none


arr = ["abc", "121", "madam", "noon", "racecar", "12321"]

print("longest palindrome in array :", long_pol(arr))


