"""
The purpose of this function is to ensure that a a string meets some basic requirements of being 
an IP address. 

Input Args: 
	ipCandidate - string whose IP canidacy is being tested. 

Output: 
	This fucniton returns true if all the reqirements are met, false if any of them are broken.   
"""
def validation(ipCandidate):
	#break the address into its components
	temp = ipCandidate.split('.')
	#if the address is missing one of the four numbers it is invalid
	if '' in temp :
		return False
	#if any of the numbers isnt within an appropriate range it is invalid
	if int(temp[0]) not in range(1, 256): 
		return False
	if int(temp[1]) not in range(0, 256) or int(temp[2]) not in range(0, 256) or int(temp[3]) not in range(0, 256): 
		return False
	return True