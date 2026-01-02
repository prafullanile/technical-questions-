#Write a program to find the longest word in a sentence.
def longest_word(str1):

	longest=""

	for i in str1:
		if len(i)>len(longest):
			longest=i
	return longest
str1="prafull Sadashiv nile"
print(longest_word(str1.split()))

#using max function
str1="prafull Sadashiv nile"
words=str1.split()

longest=max(words,key=len)
print(longest)