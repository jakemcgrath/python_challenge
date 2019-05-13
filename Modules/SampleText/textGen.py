import random
import string

"""
The purpose of this fucntion is to randomly create valid IP addresses. 

Input Args: 
	lower - a list of 4 lower bounds for each section of a valid IP
	upper - a list of 4 upper bounds for each section of a valid IP

Output: 
	Returns a string represenation of an IP address to be salted within a text file. 
"""
def sampleIPGen(lower, upper):
	#generate each section
	first =  random.sample(range(lower[0],upper[0]), 1)[0]
	second =  random.sample(range(lower[1],upper[1]), 1)[0]
	third =  random.sample(range(lower[2],upper[2]), 1)[0]
	fourth =  random.sample(range(lower[3],upper[3]), 1)[0]
	return str(first) + '.' + str(second) + '.' + str(third) + '.' + str(fourth)


"""
The purpose of this fucntion is to act as an intermediary fuction for random IP generation. 

Input Args: 
	None

Output: 
	Returns the result of sampleIPGen()
"""
def getRandomIP(): 
	return sampleIPGen([1,0,0,0],[256,256,256,256])



"""
The purpose of this fucntion is to genrate sudo-random text sudo-randomly salted randomly genrated, valid
IP addresses that will be used for testing of other modules.  
This file will never genrate two IP addresses directly next to eachother (i.e 10.0.1.3210.0.1.2.15)

Input Args: 
	outpath - where the generated text file will be stored.
	ips - the number of IP addresses to be salted in the file

Output: 
	This fucniton returns a list of the IP addresses that were added to the random text, which
	can be used for testing and comarison. This function also saves the new text file to outpath.  
"""
def textGen(outpath, ips):
	#intervals of random length that will seperate the IP addresses 
	intervals = [random.sample(range(1,500),1)[0] for i in range(ips)]
	
	text, avail = '', ''
	ips = []

	#create a charecterset which includes all printable charecters, minus numbers and '. '
	for char in string.printable: 
		if char not in string.digits and char != '.': 
			avail += char

	#populate each random interval length with randomly chosen charecters
	for span in intervals:
		for i in range(span): 
			text += random.choice(avail) # can be set to: string.printable() 
		#Generate and add an ip to the string
		a = getRandomIP()
		ips.append(a)
		text += a

	#write and save random text to file
	with open(outpath + 'generatedText.txt', 'w+') as dataFile:
		dataFile.write(text)
		dataFile.close()

	return(ips)





