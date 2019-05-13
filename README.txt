Ip Analysis Tool Challenge
--------------------------

****
See requirement.txt for list of required libraries, run library installer executable
****

Overview of package structure and function: 
	
	
This package contains six basic modules to aid in the completion of the following task:

+ Create a program that will read a given set of IPs, perform Geo IP and RDAP lookups, and accept a query to filter results

A brief overview of each module: 
+ SampleText: 
	- This module is responsible for generating sample text files that contain IP addresses that will be used by other modules for IP analysis. This module has the ability to create a wide variety of text file types with IP addresses scattered throughout in a sudo-random fashion. The spacing of the ip addresses, frequency, count, and source can all be changed within the module. Additionally, the characters used to generate the surrounding text can be controlled for, and valid IP addresses can either be read from an included database or created at random.  

+ Parse
	- The purpose of the parse module is to read in a file which contains IP addresses scattered throughout random text and extract the addresses for analysis. Two approaches were taken and are represented by separate functions within the module. The first method is a custom pattern recognition algorithm which relies on the predictable dot spacing found in IP address format. The second method implements the regex library which creates an IP address regular expression and searches the text accordingly. I have added an additional 'verbose' option to each of these factions. The reason for this is in support of the case in which both random numbers and periods are allowed in random text generation. The necessity for the verbose option is best represented with an example. Say we have the valid IP of 222.10.0.1. In a scenario where random numbers are allowed in the text generation, we have no real way of knowing if the original IP address was 222.10.0.1, 22.10.0.1, or 2.10.0.1. For the sake of thoroughness, verbose will generate every possible combination of starting and ending number sequences to ensure all IP addresses within the text can be collected for analysis. 

+ GeoIP
	- The purpose of the GeoIP module is to perform GeoIP lookups on one or many IP Addresses. In this module, the source of the GeoIp data is collected from two separate sources: an HTML request and an included database. The reason for this is that the HTML approach was relatively lightweight and easy to implement, and I was not sure if it constituted a complete GeoIP lookup solution. With respect to the database, there are two main approaches available to the user-slower and less memory intensive or faster and more memory intensive. The GeoIP database was downloaded from IP2Location, and consists of standard GeoIP data with traditional CIDR IP range format replaced with integer ranges. The slower of the two utilized a simple dictionary to store the database, while the quicker used a dictionary tree whose structure was determined by the prime factorization of the number of database entries.

+ RDAP
	- The purpose of the RDAP module was to perform RDAP lookups in a similar fashion to the GeoIP lookups. Due to the fact I was unable to find a free database with RDAP data, the only method used to obtain the data is a simple HTML request. 

+ CombinationSearch
	- This module is very lightweight, and exists for performing online GeoIP lookup, the included database lookup, and the RDAP lookup with one command. This module cannot function without the GeoIP or RDAP modules, but is not necessary to the project overall. 

+ Filter
	-This module is responsible for different filters the user can apply to filter and display the IP lookup data in a nice format. It is important to note that I didn't utilize any advanced sorting algorithms for filtering results. The purpose for this is twofold: development time constraints and the fact that 5000 dictionary entries takes virtually no time to search through. 


Caveats and Areas of Improvement
--------------------------------
1) Due to the time constant, the code is not as well tested as I would normally like it to be. I did my best to account for main use cases, but there are surely some boundary cases that have not been accounted for (especially with such a large database). 

2) The time to find all 5000 addresses from the local database on my machine using the fast method is ~10 seconds. Performing online GeoIp and RDAP lookups is bottlenecked by connection speed and your results may vary. 

3) I do not recommend performing 5000 simultaneous lookups, or you can expect a run time of ~15 minutes. 

4) I recognize that the code used for filtering data can get repetitive at times, and does not account for the needed efficiency of larger datasets. I would like to address both of these at a later date. 

5) All testing was performed on a unix machine.

6) All modules only use and account for IPv4 addresses. Again, this is due to time but I would like to address additional IPv6 functionality in the future. 

