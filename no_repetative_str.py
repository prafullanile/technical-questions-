def non_repetive(str):

	fq={ }

	for ch in str:

		fq[ch]=fq.get(ch,0)+1

	result=[ch for ch in str if fq[ch]==1]


	return result

string="programming"

print("non_repetetive character:",non_repetive(string))