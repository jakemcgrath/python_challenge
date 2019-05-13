from lxml import html
import requests
import json
from multiprocessing import Pool
from contextlib import closing
import ujson


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
	#get content and save string as a dictionary object
	return json.loads(page.content)

"""
The purpose of this function is to perfrom a batch RDAP lookup in paralell with multiprocessing

Input Args: 
	ipv4sRdap - list representation of IP addresses in question

Output: 
	This fucniton returns a list of dictionaries of RDAP information and saves the results to a JSON file.
"""
def RDAPUrlCallBatch(ipv4sRdap): 
	#make list of URLs
	ips = ipv4sRdap[:]
	for i in range(len(ipv4sRdap)): 
		ips[i] = 'https://rdap.arin.net/registry/ip/' + ipv4sRdap[i]

	#create worker pool
	with closing(Pool(None)) as p: 
		results = p.map(request, ips)
		p.terminate()

	#save results
	with open('Modules/RDAP/RDAPBatchlookupresponse', 'w+') as rsp: 
		ujson.dump(results, rsp, indent = 1)
		rsp.close()

	return results

"""
The purpose of this function is to perfrom a single RDAP lookup from a url 

Input Args: 
	ipv4 - string representation of IP address in question

Output: 
	This fucniton returns a dicitonary of RDAP information and saves the results to a JSON file. 
"""
def RDAPUrlCall(ipv4): 
	ip = 'https://rdap.arin.net/registry/ip/' + ipv4

	results = request(ip)
	with open('Modules/RDAP/RDAPlookupresponse', 'w+') as rsp: 
		ujson.dump(results, rsp, indent = 1)
		rsp.close()

	return results

