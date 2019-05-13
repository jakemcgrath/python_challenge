import Modules

#Setup: 
print('Beginning Parsing Demo')
print('Gathering IP Addresses from MaxMind database')
Modules.SampleText.realIPGen.realIPGen('realIps.txt')


#Make random text file with 5000 ips
print('Generating Random Text file and salting with 5000 real IP\'s')
ips = Modules.SampleText.textGenFromFile.textGenFromFile('generatedText.txt', 5000, 'realIps.txt')


#Parse the given text file with the two seperate methods
print('Parsing Data for IP\'s')
a = Modules.Parse.iPparse.iPparse('generatedText.txt', False)
b = Modules.Parse.smartIpParse.smartIpParse('generatedText.txt', False)

print('Recovered IP addresses saved to /Modules/Parse')

print('Custom Pattern recogntion recovered: ' + str(len(a)) +'ip\'s') 
print('Regular Expression recovered: ' + str(len(b)) +'ip\'s') 


print('Parsing Demo Complete!')
print('Beginning IP lookup Demo')

print('Generating Random Text file and salting with 50 real IP\'s')
ips = Modules.SampleText.textGenFromFile.textGenFromFile('generatedText.txt', 50, 'realIps.txt')
print('Parsing Data for IP\'s')
a = Modules.Parse.iPparse.iPparse('generatedText.txt', False)
b = Modules.Parse.smartIpParse.smartIpParse('generatedText.txt', False)

print('Custom Pattern recogntion recovered: ' + str(len(a)) +'ip\'s') 
print('Regular Expression recovered: ' + str(len(b)) +'ip\'s')

print('Creating Database')
Modules.GeoIP.Database.createDatabse()
Modules.GeoIP.Database.createDatabseFast()

print('Performing Batch GeoIp URL lookup')
a = Modules.GeoIP.ApiRequest.ApiRequestBatch(ips)
Modules.Filter.display.displayBatch(a, 'GO')

print('Performing Batch GeoIp Fast Table lookup')
a = Modules.GeoIP.Database.batchLookupFast(ips)
Modules.Filter.display.displayBatch(a, 'GT')

print('Performing Batch GeoIp RDAP lookup')
a = Modules.RDAP.RDAPUrlCall.RDAPUrlCallBatch(ips)
Modules.Filter.display.displayBatch(a, 'R')


print('IP lookup Demo Complete!')
print('Beginning Filter Demo')


a = Modules.GeoIP.ApiRequest.ApiRequestBatch(ips)
print('Performing Inquires about IP Data: ')

print('City--------')
Modules.Filter.inquiry.listCity(a, 'GO')
print('State--------')
Modules.Filter.inquiry.listState(a, 'GO')
print('Country Code--------')
Modules.Filter.inquiry.listCountryCode(a, 'GO')
print('Country--------')
Modules.Filter.inquiry.listCountries(a, 'GO')


b = Modules.Filter.filter.containsCountry(a, 'United States', 'GO')
Modules.Filter.display.displayBatch(b, 'GO')






