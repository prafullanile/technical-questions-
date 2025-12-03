str1="prafull sadashiv nile"

v=0
c=0

for ch in str1:
	if ch in ('a','e','i','o','u','A','E','I','O','U'):
		v+=1
	else:
		c+=1
print("total count of consonents and vowels is", "vowels=",v,"consonent=",c)