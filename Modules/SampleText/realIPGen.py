from netaddr import *
import random

"""
The purpose of this fucntion is to genrate real IP Addresses found in the MaxMind GeoLite Database.
The IP's in the database are in CIDR format. This function chooses a block of 1000 CIDR networks and 
generates the corresponding addresses. 
These IP's are directly used in this module to salt random text with addresses for manipulation. 

Input Args: 
	outfile - where the generated IP list will be stored.
	infile (defalt) - MaxMind database for IP generation. 

Output: 
	This fucniton does not return anything, but saves or overites the IP list at infile. 
"""

def realIPGen(outfile, infile = 'GeoLite2-City-Blocks-IPv4.csv'): 
	#open the database file
	with open(infile) as dataFile: 
		lines = dataFile.readlines()
		dataFile.close()


	#open the file to be written to
	with open(outfile,'w+') as outfile: 
		#choose a random block of 100 CIDR
		start = random.choice(range(len(lines)))
		for i in range(start, start+100):
			#convert each CIDR to IP list and write to file
			for ip in IPSet([lines[i].split(',')[0]]): 
				outfile.write(str(ip))
				outfile.write('\n')
		outfile.close()
