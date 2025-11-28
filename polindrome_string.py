def polindrome(n):

	n=n.replace(" ","").lower()

	return n == n[: : -1]

print(f"{'polidron'if polindrome("nitin") else 'not polidrom'}")