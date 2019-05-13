"""
The purpose of these functions is to print a specific trait about an IP batch

Input Args: 
	data - list of dictionary results
	typ - type of lookup perfromed

Output: 
	This fucniton prints requested results
"""

def listCountries(data, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['country_name'])
			
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + item)
				i += 1
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['country'])
	
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + item)
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')

def listCountryCode(data, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['country_code'])
			
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + item)
				i += 1
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['countryCode'])
	
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + item)
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')

def listPostalCode(data, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['postal'])
			
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['zip'])
	
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')

def listState(data, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['state'])
			
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['region'])
	
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')


def listCity(data, typ):
	if 'GO' in typ or 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['city'])
			
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')
		

def listCoords(data, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			retlist.append([ip['latitude'], ip['longitude']])
			
		if retlist != []:
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append([ip['lat'], ip['lon']])
		if retlist != []:
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1

	if 'R' in typ or 'A' in typ:
		print('Query not available for selected search method!')

def listTimes(data, typ):
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			retlist.append(ip['time'])
	
		if retlist != []:
			retlist = list(dict.fromkeys(retlist))
			i = 1
			for item in retlist: 
				print('[' + str(i) + '] ' + str(item))
				i += 1

	if 'R' in typ or 'A' in typ or 'GO' in typ:
		print('Query not available for selected search method!')

