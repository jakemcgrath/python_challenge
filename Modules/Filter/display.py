"""
The purpose of these functions is to display search result criteria

Input Args: 
	data - list of dictionary results
	typ - type of lookup perfromed

Output: 
	This fucniton prints requested results
"""

def displaySingle(data, typ): 
	if type(data) is dict: 
		if 'GO' in typ:
			print('\n\n')
			print("{:<20} {:<15}".format('Online GeoIP Results For: ', data['IPv4']))
			print ("{:<20} {:<20}".format('Category','Result'))
			print("{:<20}".format('_'*40))

			print ("{:<20} {:<20}".format('Country: ', data['country_name']))
			print ("{:<20} {:<20}".format('Country Code: ', data['country_code']))
			print ("{:<20} {:<20}".format('Postal Code: ', data['postal']))
			print ("{:<20} {:<20}".format('State: ', data['state']))
			print ("{:<20} {:<20}".format('City: ', data['city']))
			print ("{:<20} {:<20}".format('Latitude: ', data['latitude']))
			print ("{:<20} {:<20}".format('Longitude: ', data['longitude']))

		if 'GT' in typ:
			print('\n\n')
			print("{:<20} {:<15}".format('Table GeoIP Results For: ', data['ip']))
			print ("{:<20} {:<20}".format('Category','Result'))
			print("{:<20}".format('_'*40))

			print ("{:<20} {:<20}".format('IP Interger Range: ', data['ipFrom'][1:-1] + '-'+ data['ipTo'][1:-1]))
			print ("{:<20} {:<20}".format('Country: ', data['country'][1:-1]))
			print ("{:<20} {:<20}".format('Country Code: ', data['countryCode'][1:-1]))
			print ("{:<20} {:<20}".format('Postal Code: ', data['zip'][1:-1]))
			print ("{:<20} {:<20}".format('State: ', data['region'][1:-1]))
			print ("{:<20} {:<20}".format('City: ', data['city'][1:-1]))
			print ("{:<20} {:<20}".format('Latitude: ', data['lat'][1:-1]))
			print ("{:<20} {:<20}".format('Longitude: ', data['lon'][1:-1]))
			print ("{:<20} {:<20}".format('Time Zone: ', data['time']))

		if 'R' in typ: 
			print('\n\n')
			print("{:<20} {:<15}".format('RDAP Lookup Results For: ', data['links'][0]['value'].split('/')[-1]))
			print ("{:<20} {:<20}".format('Category','Result'))
			print("{:<20}".format('_'*40))

			print ("{:<20} {:<20}".format('Handle: ', data['handle']))
			print ("{:<20} {:<20}".format('Name: ', data['name']))
			print ("{:<20} {:<20}".format('Port 43: ', data['port43']))
			print ("{:<20} {:<20}".format('IP Version: ', data['ipVersion']))
			print ("{:<20} {:<20}".format('Start Address: ', data['startAddress']))
			print ("{:<20} {:<20}".format('End Address: ', data['endAddress']))

			
		if 'A' in typ: 
			dgt = data[0]
			dgo = data[1]
			dt = data[2]

			print('\n\n')
			print("{:<20} {:<15}".format('All IP Results For: ', dgo['IPv4']))
			print ("{:<20} {:<20}".format('Category','Result'))
			print("{:<20}".format('_'*40))

			print('\nOnline GeoIP:')
			print ("{:<20} {:<20}".format('Country: ', dgo['country_name']))
			print ("{:<20} {:<20}".format('Country Code: ', dgo['country_code']))
			print ("{:<20} {:<20}".format('Postal Code: ', dgo['postal']))
			print ("{:<20} {:<20}".format('State: ', dgo['state']))
			print ("{:<20} {:<20}".format('City: ', dgo['city']))
			print ("{:<20} {:<20}".format('Latitude: ', dgo['latitude']))
			print ("{:<20} {:<20}".format('Longitude: ', dgo['longitude']))
			print('\nTable GeoIP')
			print ("{:<20} {:<20}".format('IP Interger Range: ', dgt['ipFrom'][1:-1] + '-'+ dgt['ipTo'][1:-1]))
			print ("{:<20} {:<20}".format('Country: ', dgt['country'][1:-1]))
			print ("{:<20} {:<20}".format('Country Code: ', dgt['countryCode'][1:-1]))
			print ("{:<20} {:<20}".format('Postal Code: ', dgt['zip'][1:-1]))
			print ("{:<20} {:<20}".format('State: ', dgt['region'][1:-1]))
			print ("{:<20} {:<20}".format('City: ', dgt['city'][1:-1]))
			print ("{:<20} {:<20}".format('Latitude: ', dgt['lat'][1:-1]))
			print ("{:<20} {:<20}".format('Longitude: ', dgt['lon'][1:-1]))
			print ("{:<20} {:<20}".format('Time Zone: ', dgt['time']))
			print('\nRDAP Lookup')
			print ("{:<20} {:<20}".format('Handle: ', dt['handle']))
			print ("{:<20} {:<20}".format('Name: ', dt['name']))
			print ("{:<20} {:<20}".format('Port 43: ', dt['port43']))
			print ("{:<20} {:<20}".format('IP Version: ', dt['ipVersion']))
			print ("{:<20} {:<20}".format('Start Address: ', dt['startAddress']))
			print ("{:<20} {:<20}".format('End Address: ', dt['endAddress']))

	else: 
		print('Data is not of type dict. Cannot be displayed!')
def displayBatch(data, typ): 
	if type(data) is list: 
		if 'GO' in typ:
			print('\n\n')
			print("{:<20}".format('Online Batch GeoIP Results: ([' + str(len(data)) + ']) '))
			print ("{:<20} {:<20} {:<20}".format('', 'Category','Result'))
			print("{:<20}".format('_'*60))

			i = 1
			for ip in data: 
				print ("{:<20} {:<20} {:<20}".format('['+ str(i) + ']  ' +ip['IPv4'], '', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'Country: ', ip['country_name']))
				print ("{:<20} {:<20} {:<20}".format('', 'Country Code: ', ip['country_code']))
				print ("{:<20} {:<20} {:<20}".format('', 'Postal Code: ', ip['postal']))
				print ("{:<20} {:<20} {:<20}".format('', 'State: ', ip['state']))
				print ("{:<20} {:<20} {:<20}".format('', 'City: ', ip['city']))
				print ("{:<20} {:<20} {:<20}".format('', 'Latitude: ', ip['latitude']))
				print ("{:<20} {:<20} {:<20}".format('', 'Longitude: ', ip['longitude']))
				print("{:<20}".format('_'*60))
				i += 1
		if 'GT' in typ:
			print('\n\n')
			print("{:<20}".format('Table GeoIP Batch Results: ([' + str(len(data)) + ']) '))
			print ("{:<20} {:<20} {:<20}".format('', 'Category','Result'))
			print("{:<20}".format('_'*60))

			i = 1
			for ip in data: 
				print ("{:<20} {:<20} {:<20}".format('['+ str(i) + ']  ' +ip['ip'], '', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'IP Interger Range: ', ip['ipFrom'][1:-1] + '-'+ ip['ipTo'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Country: ', ip['country'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Country Code: ', ip['countryCode'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Postal Code: ', ip['zip'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'State: ', ip['region'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'City: ', ip['city'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Latitude: ', ip['lat'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Longitude: ', ip['lon'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Time Zone: ', ip['time']))
				print("{:<20}".format('_'*60))
				i+=1

		if 'R' in typ:
			print('\n\n')
			print("{:<20}".format('RDAP Lookup Batch Results: ([' + str(len(data)) + ']) '))
			print ("{:<20} {:<20} {:<20}".format('', 'Category','Result'))
			print("{:<20}".format('_'*60))

			i = 1
			for ip in data:
				print ("{:<20} {:<20} {:<20}".format('['+ str(i) + ']  ' +ip['links'][0]['value'].split('/')[-1], '', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'Handle: ', ip['handle']))
				print ("{:<20} {:<20} {:<20}".format('', 'Name: ', ip['name']))
				print ("{:<20} {:<20} {:<20}".format('', 'Port 43: ', ip['port43']))
				print ("{:<20} {:<20} {:<20}".format('', 'IP Version: ', ip['ipVersion']))
				print ("{:<20} {:<20} {:<20}".format('', 'Start Address: ', ip['startAddress']))
				print ("{:<20} {:<20} {:<20}".format('', 'End Address: ', ip['endAddress']))
				print("{:<20}".format('_'*60))
				i += 1

		if 'A' in typ: 
			dgt = data[0]
			dgo = data[1]
			dt = data[2]

			print('\n\n')
			print("{:<20}".format('All IP Batch Results: ([' + str(len(dgt)) + ']) '))
			print ("{:<20} {:<20} {:<20}".format('', 'Category','Result'))
			print("{:<20}".format('_'*60))

			i = 1
			for t, o, r in zip(dgt, dgo, dt): 
				print ("{:<20} {:<20} {:<20}".format('['+ str(i) + ']  ' +o['IPv4'], '', ''))
				print('\n')
				print ("{:<20} {:<20} {:<20}".format('', 'Online GeoIP:', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'Country: ', o['country_name']))
				print ("{:<20} {:<20} {:<20}".format('', 'Country Code: ', o['country_code']))
				print ("{:<20} {:<20} {:<20}".format('', 'Postal Code: ', o['postal']))
				print ("{:<20} {:<20} {:<20}".format('', 'State: ', o['state']))
				print ("{:<20} {:<20} {:<20}".format('', 'City: ', o['city']))
				print ("{:<20} {:<20} {:<20}".format('', 'Latitude: ', o['latitude']))
				print ("{:<20} {:<20} {:<20}".format('', 'Longitude: ', o['longitude']))
				print('\n')
				print ("{:<20} {:<20} {:<20}".format('', 'Table GeoIP', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'IP Interger Range: ', t['ipFrom'][1:-1] + '-'+ t['ipTo'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Country: ', t['country'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Country Code: ', t['countryCode'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Postal Code: ', t['zip'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'State: ', t['region'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'City: ', t['city'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Latitude: ', t['lat'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Longitude: ', t['lon'][1:-1]))
				print ("{:<20} {:<20} {:<20}".format('', 'Time Zone: ', t['time']))
				print ("{:<20} {:<20} {:<20}".format('', 'RDAP Lookup', ''))
				print ("{:<20} {:<20} {:<20}".format('', 'Handle: ', r['handle']))
				print ("{:<20} {:<20} {:<20}".format('', 'Name: ', r['name']))
				print ("{:<20} {:<20} {:<20}".format('', 'Port 43: ', r['port43']))
				print ("{:<20} {:<20} {:<20}".format('', 'IP Version: ', r['ipVersion']))
				print ("{:<20} {:<20} {:<20}".format('', 'Start Address: ', r['startAddress']))
				print ("{:<20} {:<20} {:<20}".format('', 'End Address: ', r['endAddress']))
				print("{:<20}".format('_'*60))
				i += 1
	else: 
		print('Data is not of type List(Dict). Cannot be displayed!')
