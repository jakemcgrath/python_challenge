from netaddr import *
import ujson
from multiprocessing import Pool
from contextlib import closing
import itertools
from concurrent.futures import ThreadPoolExecutor
import threading

"""
The purpose of this funciton is to create a dicitonary object of the IP2Locaiton database and
store it in a file as a JSON object to be used later. The database keys are IP ranges represented as in integer.

Input Args: 
	infile(default) - databse name

Output: 
	This fucntion writes the dictionary object to a JSON file. 
"""
def createDatabse(infile = 'IP2LOCATION-LITE-DB11.CSV'): 
	data = {}

	#read lines of csv
	with open(infile) as dataFile: 
		lines = dataFile.readlines()
		dataFile.close()

	#make dictionary
	for i in range(1,len(lines)):
		data[(lines[i].split(',')[0][1:-1])] = lines[i]

	#write to file
	with open('Modules/GeoIP/ipv4DatabseObject', 'w+') as db: 
		ujson.dump(data, db)
		db.close()

"""
The purpose of this funciton is to create a hybrid dicitonary-tree object of the IP2Locaiton database and
store it in a file as a JSON object to be used later. The database keys are IP ranges represented as in integer.

Input Args: 
	infile(default) - databse name

Output: 
	This fucntion writes the tree-dictionary object to a JSON file. 
"""
def createDatabseFast(infile = 'IP2LOCATION-LITE-DB11.CSV'): 
	data = {}

	#read lines of csv
	with open(infile) as dataFile: 
		lines = dataFile.readlines()
		dataFile.close()

	#make primary dictionary
	for i in range(1,len(lines)):
		data[(lines[i].split(',')[0][1:-1])] = lines[i]


	data2 = {}

	#sort values of first diciotnary
	keys = list(data.keys())
	values = list(data.values())
	keys, values = zip(*sorted(zip(keys, values)))

	#ensure they are in asending order
	keys = list(keys)
	values= list(values)
	keys.reverse()
	values.reverse()

	#create a second layer of range values, size determined from prime factorization of size of csv
	for i in range(2542, len(list(data.keys())), 2543):
		newkey = keys[i]
		subdict = dict(zip(keys[i-2543:i], values[i-2543:i]))
		data2[newkey] = subdict

	#write to file
	with open('Modules/GeoIP/ipv4DatabseObjectFast', 'w+') as db: 
		ujson.dump(data2, db, indent = 4)
		db.close()

"""
The purpose of this funciton is to load a precreated database from a JSON object  

Input Args: 
	infile(default) - JSON object location

Output: 
	This function returns tree-dictionary object 
"""
def loadDatabaseFast(infile = 'Modules/GeoIP/ipv4DatabseObjectFast'): 
	with open(infile) as dataFile: 
		return ujson.load(dataFile)

"""
The purpose of this funciton is to load a precreated database from a JSON object  

Input Args: 
	infile(default) - JSON object location

Output: 
	This function returns dictionary object 
"""
def loadDatabase(infile = 'Modules/GeoIP/ipv4DatabseObject'): 
	with open(infile) as dataFile: 
		return ujson.load(dataFile)

"""
The purpose of this funciton is to perform a single lookup from the tree-dicitonary database 

Input Args: 
	ipv4 - IP address in question

Output: 
	This function returns a dictionary with GeoIP information 
"""
def singleLookupFast(ipv4):
	#dict keys
	headers = ['ipFrom', 'ipTo', 'countryCode', 'country', 'region', 'city', 'lat', 'lon', 'zip', 'time', 'ip']
	#load the database
 	data = loadDatabaseFast()
 	#convert IP to an integer
	ip = int(IPAddress(ipv4))
	#search the first layer of the dictionary
	dict1 = data[str(max(key for key in map(int, data.keys()) if key <= ip))]
	#search the sub-dictionary returned from the primary layer and return the corresponding dict
	return dict(zip(headers, dict1[str(max(key for key in map(int, dict1.keys()) if key <= ip))].split(',')+ [ipv4]))

"""
The purpose of this funciton is to perform a single lookup from the dicitonary database 

Input Args: 
	ipv4 - IP address in question

Output: 
	This function returns a dictionary with GeoIP information 
"""
def singleLookup(ipv4):
	#dict keys
	headers = ['ipFrom', 'ipTo', 'countryCode', 'country', 'region', 'city', 'lat', 'lon', 'zip', 'time', 'ip']
	#load the database
 	data = loadDatabase()
 	#convert IP to an integer
	ip = int(IPAddress(ipv4))
	#search the dicitonary and return results
	return dict(zip(headers, data[str(max(key for key in map(int, data.keys()) if key <= ip))].split(',')+ [ipv4]))


"""
Helper functions for multiprocess batch lookup functions

Input Args: 
	a_b - database and ipv4 address

Output: 
	These functions return a singe search call with a_b split into a and b 
"""
def searchStarFast(a_b): 
	return searchFast(*a_b)

def searchStar(a_b): 
	return search(*a_b)


"""
Helper functions for multiprocess batch lookup functions

Input Args: 
	ipv4 - single IP address in quesiton
	data - database dictionary

Output: 
	These functions return a dictionary with GeoIP information
"""
def searchFast(ipv4, data):
	headers = ['ipFrom', 'ipTo', 'countryCode', 'country', 'region', 'city', 'lat', 'lon', 'zip', 'time', 'ip']
	ip = int(IPAddress(ipv4))
	dict1 = data[str(max(key for key in map(int, data.keys()) if key <= ip))]
	return dict(zip(headers, dict1[str(max(key for key in map(int, dict1.keys()) if key <= ip))].split(',') + [ipv4]))

def search(ipv4, data):
	headers = ['ipFrom', 'ipTo', 'countryCode', 'country', 'region', 'city', 'lat', 'lon', 'zip', 'time', 'ip']
	ip = int(IPAddress(ipv4))
	return dict(zip(headers, data[str(max(key for key in map(int, data.keys()) if key <= ip))].split(',')+ [ipv4]))


"""
The purpose of these functions is to perfrom multiple IP lookups in paralell using multiprocessing

Input Args: 
	ipv4s - list of IP's in quesiton

Output: 
	These functions return a list of dictionaries with GeoIP information
"""
def batchLookupFast(ipv4s): 
	data = loadDatabaseFast()
	#Start pool with eight workers
	with ThreadPoolExecutor(8) as executor:
		results = executor.map(searchStarFast, itertools.izip(ipv4s, itertools.repeat(data)))
	return list(results)

def batchLookup(ipv4s):
	data = loadDatabase()
	#Start pool with eight workers
	with ThreadPoolExecutor(8) as executor:
		results = executor.map(searchStar, itertools.izip(ipv4s, itertools.repeat(data)))
	end = time.time()
	return list(results)


	
	


	

