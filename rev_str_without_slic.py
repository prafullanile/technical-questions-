str1=input("enter string")

rev_str=""

for ch in str1:
	rev_str=ch+rev_str

print("reverse string without slicing", rev_str)