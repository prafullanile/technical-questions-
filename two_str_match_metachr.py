def match_str(a,b):

	import re

	pattern="^" +b.replace("?",".").replace("*",".*")+"$"

	return re.match (pattern,a) is not None


print(match_str("hello","h?llo"))

print(match_str("carrr","c*r"))