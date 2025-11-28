def frequency(str):

	fq={}

	for ch in str:

		if ch in fq:

			fq[ch]+=1


		else:

			fq[ch]=1

	return fq

string="hello world"
print(frequency(string))