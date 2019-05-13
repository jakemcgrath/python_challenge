"""
The purpose of these functions is to refine an IP list depending on user criteria

Input Args: 
	data - list of dictionary results
	typ - type of lookup perfromed

Output: 
	This fucniton returns a refined dicitonary 
"""

def containsCountry(data, country, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_name'] == country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['country'] == country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def containsCountries(data, country, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_name'] in country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['country'] in country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def doesNotContainCountry(data, country, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_name'] != country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['country'] != country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def doesNotContainCountries(data, country, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_name'] not in country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['country'] not in country:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def containsCountryCode(data, countryCode, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_code'] == countryCode:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['countryCode'] == countryCode:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def containsCountryCodes(data, countryCodes, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_code'] in countryCodes:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['countryCode'] in countryCodes:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def doesNotContainCountryCode(data, countryCode, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_code'] != countryCode:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['countryCode'] != countryCode:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

def doesNotContainCountryCodes(data, countryCodes, typ):
	if 'GO' in typ:
		retlist = []
		for ip in data: 
			if ip['country_code'] not in countryCodes:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None
			
	if 'GT' in typ:
		retlist = []
		for ip in data: 
			if ip['countryCode'] not in countryCodes:
				retlist.append(ip)

		if retlist != []:
			return retlist

		else: 
			print('No Mathces Found!')
			return None

	if 'R' in typ or 'A' in typ:
		print('Filter not available for selected search method!')

