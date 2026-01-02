#Write a program to find common elements between two lists

#using set and & operater for intersection
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]

com_ele=list(set(l1) & set(l2))

print("common element in both list", com_ele)

#using list comprehension

common=[i for i in l1 if i in l2]
print(common)

#usingloop

comm = []

for i in l1:
    if i in l2:
        comm.append(i)

print(comm)