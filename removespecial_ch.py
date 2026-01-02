#Write a program to remove special characters from a string.

str1="prafullnile9@gmail.com##"

result="".join(ch for ch in str1 if ch.isalnum())
print(result)