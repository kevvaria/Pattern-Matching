# Name: Keval Varia
# Assignment 13: Pattern Matching
# Class: Data Structures

'''
Program Details:
- this program includes three different pattern matching algorithms:
 a. Brute Force: where we compare each value of the pattern to that of the text.
 b. Boyer Moore: compare each value of the pattern to the while skipping non-existent values using a lastc function.
 c. Knutt Morris Pratt: Compare the pattern to the text based off a failure function 
 - each pattern will return the number of comparisions taken to find the pattern in the text.
'''
#-------------------------------------------------------------------------------
# string to list:
def stringToList(text):
	vals = []
	for x in range(len(text)):
		vals.append(text[x])
	return vals


# Brute Force Method
def bruteForce(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while (j < len(pattern) and text[i+j] == pattern[j]):
            j += 1
            if(j == len(pattern)):
                return i
    return -1

#-------------------------------------------------------------------------------

# Boyer Moore Method
def boyerMoore(text, pattern):
	if len(pattern) == 0:
		return 0
	last = {}
	for k in range(len(pattern)):
		last[pattern[k]] = k
	i = len(pattern) - 1
	k = len(pattern) - 1
	while i < len(text):
		if text[i] == pattern[k]:
			if k == 0:
				return i
			else:
				i -= 1
				k -= 1
		else:
			j = last.get(text[i], -1)
			i += (len(pattern) - min(k, j+1))
			k = len(pattern) - 1
	return -1

# Last-C function for Boyer Moore Algorithm
def lastc(pattern, value):
	index = -1
	for i in range(len(pattern)):
		if (pattern[i] == value):
			index = i
	return index

#-------------------------------------------------------------------------------


# Knutt Morris Pratt
def KMP(text, pattern):
	if len(pattern) == 0:
		return 0
	   	fail = failFunction(pattern)
	   	j = 0
	   	k = 0
	   	while j < len(text):
	   		if (text[j] == pattern[k]):
	   			if k == len(pattern) - 1:
	   				return j - len(pattern) + 1
				j += 1
				k += 1
	   		elif k > 0:
	   			k = fail[k-1]
	   		else:
	   			j += 1
	   	return -1

# Failure Function for Knutt Morris Pratt Algorithm
def failFunction(pattern):
	fail=[0]*len(pattern)
	j=1
	k=0
	while j<len(pattern):
		if(pattern[j]==pattern[k]):
			fail[j]=k+1
			j+=1
			k+=1
		elif k>0:
			k=fail[k-1]
		else:
			j+=1
	return fail

#-------------------------------------------------------------------------------

def main():
	# variable declaration
	text = "aaabcaadaabaaa"
	pattern = "aabaaa"

	# convert strings to list for comparision
	listText = stringToList(text)
	listPattern = stringToList(pattern)

	# print list version of the text
	print "\nList:"
	print listText

	# print list version of the pattern
	print "\nPattern:"
	print listPattern

	# Print number of comparisions for each algorithm
	print "\nNumber of Comparisions:"
	print ("Brute Force:", (bruteForce(listText, listPattern) + len(listPattern)))
	print ("Boyer Moore:", (boyerMoore(listText, listPattern) + 1))
	print ("Knutt Morris Pratt:", (KMP(listText, listPattern)))
	print "\n"

	print "Last-C for Boyer Moore:"
	for index, item in enumerate(pattern):
		print item, lastc(pattern, item)
	print "\n"

	print "Failure Function:"
	fail = failFunction(listPattern)
	for a,b in zip(pattern, fail):
		print a, b
	print "\n"
#-------------------------------------------------------------------------------

# function call to initialize the program
main()
