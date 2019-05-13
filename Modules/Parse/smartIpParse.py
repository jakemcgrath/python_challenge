import verboseIp
import validation
import regex
import ujson

"""
The purpose of this function is to use the regural expression library to find IP addresses within
provided text.

Input Args: 
	filename - filepath to the desired text file for analyizing. 
	verbose - Generate all possible combinaitons of starting and ending segement to protect agiainst random
	number contamination

Output: 
	This fucniton returns a list of the IP addresses found in the text and saves addresses to file.
"""

def smartIpParse(filename, verbose): 
	#open the text file
	with open(filename, 'r') as dataFile: 
		text = dataFile.readlines()
		dataFile.close() 

	#create one large string from file contents
	line = (''.join(text)).strip('.')	

	#define regular expression in form of IP
	ipCandidates = regex.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)

	#if Verbose...
	if verbose == True:  
		ipCandidates += verboseIp.verboseIp(ipCandidates)

	#remove leading zeros -- 010.X == 10.X
	for i in range(len(ipCandidates)): 
		if ipCandidates[i][0] == '0': 
			while ipCandidates[i][0] == '0':
				ipCandidates[i] = ipCandidates[i][1:]

	with open('Modules/Parse/smartIpParse', 'w+') as rsp: 
		ujson.dump(ipCandidates, rsp, indent = 1)
		rsp.close()

	return ipCandidates