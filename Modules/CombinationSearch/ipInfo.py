import Modules.GeoIP as GeoIP
import Modules.RDAP as RDAP


"""
The purpose of these funcitons is to perfrom GeoIP from url, GeoIP from table, and RDAP lookups 

Input Args: 
	ip - string representation of IP address in question

Output: 
	This fucniton returns a list of dicitonaries of results. 

	TODO - Multiprocessing to process searches in paralell
"""
def searchIp(ip):
	return[GeoIP.Database.singleLookupFast(ip), 
	GeoIP.ApiRequest.ApiRequest(ip), 
	RDAP.RDAPUrlCall.RDAPUrlCall(ip)]

def searchIpBatch(ips):
	return[GeoIP.Database.batchLookupFast(ips), 
	GeoIP.ApiRequest.ApiRequestBatch(ips), 
	RDAP.RDAPUrlCall.RDAPUrlCallBatch(ips)]