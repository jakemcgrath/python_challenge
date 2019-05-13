import string
import verboseIp
import validation
import ujson



"""
The purpose of this function is to use the regualr and predictable structure of an IP address to
find occurances within random text. 

Input Args: 
	filename - text file with random text to be read
	verbose - boolean to indicate whether or not additional potential addresses will be
	made in the event of random number contamination 

Output: 
	This fucniton returns a list found and potential IP addresses and saves addresses to file
"""
def iPparse(filename, verbose): 
	#open the text file
	with open(filename, 'r') as dataFile: 
		text = dataFile.readlines()
		dataFile.close() 

	#the only charecters we care about are numbers and periods
	validChars = string.digits + '.'
	primaryFilter = ''

	#make one long string and remove starting and ending periods (never part of an IP address)
	line = (''.join(text)).strip('.')
	i = 0
	while i < len(line):
		#if the charecter is a number or period
		if line[i] in validChars:
			#if it is a period in an ip address, the previous and next charecters must be a number
			#if false, we know this period isnt part of an address so we can discard it
			if line[i] == '.' and (line[i-1] not in string.digits or line[i+1] not in string.digits): 
				i+=1
				continue
			#if it is a number or valid period, add it to a fresh string
			else: 
				primaryFilter += line[i]
				i += 1
		else: 
			#if the char is not a number or period, ad a string of five x's to the fresh string
			while i <len(line) and line[i] not in validChars: 
				i +=1
			primaryFilter += 'xxxxx'

	#map out the location of every fresh dot in the new string
	dotLocals = [index for index, char in enumerate(primaryFilter) if char == '.']
	#the index difference between teh first and last period will be >=4 and <=8 
	#calculate all of these differences, and if they match the criteria, add thier location to a fresh array
	diffrences = [[dotLocals[i], dotLocals[i+2]] for i in range(0, len(dotLocals)-2) if dotLocals[i+2]-dotLocals[i] >=4 and dotLocals[i+2]-dotLocals[i] <=8]
	
	ipCandidates = []
	#for each set of perods that is a valid distance apart
	for diff in diffrences: 
		#remove any x's that are on the start or end
		#this might happen becuase the first and last number can be 1, 2, or 3 digits long
		temp = (primaryFilter[diff[0]-3:diff[1]+4]).translate(None, 'x')
		#remove leading zeros
		while temp[0] == '0':
			temp = temp[1:]
		#if there are three points, it is valid and we can add it to the array
		if temp.count('.') == 3:
			ipCandidates.append(temp)

	#if the user wants to be cautios and generate more
	if verbose == True:  
		ipCandidates += verboseIp.verboseIp(ipCandidates)

	with open('Modules/Parse/IpParse', 'w+') as rsp: 
		ujson.dump(ipCandidates, rsp, indent = 1)
		rsp.close()

	return ipCandidates
	


