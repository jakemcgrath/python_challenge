import validation	

"""
The purpose of this function is to generate possible varaions of the first number (illustrated below): 
	given: 123
	returns: 123, 23, 3 (because a 1 or a 12 could have been potentially added to the front randomly)

Input Args: 
	sequence - start number we will permute  

Output: 
	This fucniton returns a list new permuatiaons
"""
def genCombosStart(sequence): 
	if len(sequence) == 3: 
		return [sequence[:], sequence[-2:], sequence[-1:]]
	elif len(sequence) == 2: 
		return [sequence[:], sequence[-1:]]
	else: 
		return [sequence[:]]


"""
The purpose of this function is to generate possible varaions of the last number (illustrated below): 
	given: 123
	returns: 123, 12, 1 (because a 2 or a 21 could have been potentially added to the end randomly)

Input Args: 
	sequence - end number we will permute  

Output: 
	This fucniton returns a list new permuatiaons
"""
def genCombosEnd(sequence): 
	if len(sequence) == 3: 
		return [sequence[:], sequence[:-1], sequence[:-2]]
	elif len(sequence) == 2: 
		return [sequence[:], sequence[:-1]]
	else: 
		return [sequence[:]]		

"""
The purpose of this function is to create varations of an IP address by altering the first and last 
number sets taht could have potentially added on to during random text generation. 

Input Args: 
	ipCandidates - list of IP addresses for which the permutations will be generated.  

Output: 
	This fucniton returns a list new, valid  IP addresses that have been permuted from the original list.   
"""
def verboseIp(ipCandidates):
	new = []
	#for each IP in list
	for candidate in ipCandidates:
		#break the canidate into seperate parts, and permute start and end values
		temp = candidate.split('.')
		fronts = genCombosStart(temp[0])
		rears = genCombosEnd(temp[3])

		#combine all new starts and ends with exissting middles
		for front in fronts: 
			for rear in rears: 
				permuation = front + '.' + temp[1] + '.' + temp[2] + '.' +rear
				#if our address is both valid and isnt the same as the original
				if (permuation) != candidate and validation.validation(permuation) == True: 
					#remove leading zeros
					while permuation[0] == '0':
						permuation = permuation[1:]
					new.append(permuation)
	#return list removing duplicates
	return list(dict.fromkeys(new))