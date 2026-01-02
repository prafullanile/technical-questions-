#Write a program to convert two lists into a dictionary.

#using zip function
key=[1,2,3,4]
values=['a','b','c','d']

re=dict(zip(key,values))
print(re)

#using loop
result={}

for i in range(len(key)):
	result[key[i]]=values[i]

print(result)