import random
import string

"""
The purpose of this fucntion is to genrate sudo-random text sudo-randomly salted with real IP Addresses found 
in the MaxMind GeoLite Database that will be used for testing of other modules.  
This file will never genrate two IP addresses directly next to eachother (i.e 10.0.1.3210.0.1.2.15)

Input Args: 
	outpath - where the generated text file will be stored.
	ips - the number of IP addresses to be salted in the file
	ipfile - file containing real IP addresses for salting

Output: 
	This fucniton returns a list of the IP addresses that were added to the random text, which
	can be used for testing and comarison. This function also saves the new text file to outpath.  
"""

def textGenFromFile(outpath, ips, ipfile): 
	#intervals of random length that will seperate the IP addresses
	intervals = [random.sample(range(1,500),1)[0] for i in range(ips)]

	text, avail = '', ''
	ips, added = [], []

	#open the ip file and save its contents to an array
	with open(ipfile) as ipFile: 
		ips = ipFile.readlines()
		ipFile.close()

	#create a charecterset which includes all printable charecters, minus numbers and '. '
	for char in string.printable: 
		if char not in string.digits and char != '.': 
			avail += char

	#populate each random interval length with randomly chosen charecters
	for span in intervals:
		for i in range(span): 
			text += random.choice(avail) # can be set to: string.printable 
		#randomly chose and add an ip to the string
		a = random.choice(ips)
		text += a[:-1]
		added.append(a[:-1])

	#write and save random text to file
	with open(outpath, 'w+') as dataFile:
		dataFile.write(text)
		dataFile.close()

	return(added)





