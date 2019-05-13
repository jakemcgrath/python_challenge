from lxml import html
import requests
import ujson
from multiprocessing import Pool
from contextlib import closing

"""
Helper function for the ApiRequestBatch() and ApiRequest() funcitons. 
Perfroms a single search or one of many in a pooled process. 

Input Args: 
	url - url to request

Output: 
	This fucntion returns a dicitonary of GeoIP informaiton
"""
def request(url):
	#make request
	page = requests.get(url)
	#get content and remove unused charecters so the string can be converted to a dictionary object
	dictString = page.content[9:-1]
	return ujson.loads(dictString)


"""
The purpose of this function is to perfrom a batch GeoIP lookup in paralell with multiprocessing

Input Args: 
	ipv4s - list representation of IP addresses in question

Output: 
	This fucniton returns a list of dictionaries of GeoIP information and saves the results to a JSON file.
"""
def ApiRequestBatch(ipv4s): 
	#create a list of urls
	ips = ipv4s[:]
	for i in range(len(ipv4s)): 
		ips[i] = 'https://geoip-db.com/jsonp/' + ipv4s[i]

	#open multiple processes to quickly process results in paralell
	with closing(Pool(None)) as p: 
		results = p.map(request, ips)
		p.terminate()

	#write results
	with open('Modules/GeoIP/GeoIPURLBatchlookupresponse', 'w+') as rsp: 
		ujson.dump(results, rsp, indent = 1)
		rsp.close()

	return results

"""
The purpose of this function is to perfrom a single GeoIP lookup from a url 

Input Args: 
	ipv4 - string representation of IP address in question

Output: 
	This fucniton returns a dicitonary of GeoIP information and saves the results to a JSON file. 
"""
def ApiRequest(ipv4): 
	ip = 'https://geoip-db.com/jsonp/' + ipv4

	results = request(ip)

	#write results
	with open('Modules/GeoIP/GeoIPURLSinglelookupresponse', 'w+') as rsp: 
		ujson.dump(results, rsp, indent = 1)
		rsp.close()

	return results


