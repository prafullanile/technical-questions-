#Write a program to reverse the order of words in a string

str1="prafull Sadashiv nile"

word=str1.split()

reverse_words=word[::-1]

separated=" ".join(reverse_words)
print(separated)
