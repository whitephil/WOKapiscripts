'''
READ THESE COMMENTS BEFORE ATTEMPTING TO USE
-Your institution must have a subscription to Web Services Expanded
-The WOS API is a SOAP API --learn how SOAP works
-Review the Web of Science Web Services Expanded documentation thoroughly before using this script.
-Review SUDS documentation and examples: https://bitbucket.org/jurko/suds/wiki/Original%20Documentation 
-Learn how to use SUDS
-I used suds-jurko 0.6. Other suds packages threw errors.
-This script does not include the authentication process (though this could be added).
-I authenticate before running script by sending simple xml message via Postman
-The authentication request must contain institutional username and password encoded into Base64 as a header as well as SOAP envelope in xml
-When done correctly, you'll recieve an xml message in return with session ID (SID)
-Review the authentication docs & the request docs
-I commented this script heavily to make its use as clear as possible
-With all comments removed, this is only 13 lines of code, remove comments if you want to declutter.
-You'll have to populate a csv with a list of UIDs (WoS accession numbers) of all the pubs you want to pull the citations from.
-This very simple script works, though perhaps there is a more efficient way of writing it? :-)
'''

from suds.client import Client #suds is the SOAP api client
from time import sleep #allows for throttling of requests to >.5 second
import csv #allows for reading a csv that contains list of UIDs that will run through the for loop


f = open('yourcsv.csv')
         #^csv containing list of WOS UID numbers  

csv_f = csv.reader(f)

saveFile = open('outputfile.xml','ab')
# new output xml file^            ^appends citations from each UID into new file instead of overwriting   

for uid in csv_f:
    sleep(0.6)#throttles to 1 request every 0.6 seconds to comply with terms of service
    url = 'http://search.webofknowledge.com/esti/wokmws/ws/WokSearch?wsdl'
    client = Client(url, retxml=True)#<tells api to return xml
    client.set_options(headers={'Content-type':'text/xml', 'Cookie':'SID= '})
                               #^Tells api header is xml^                ^session ID goes here

    rparams = orderedDict([('firstRecord' : 1, 'count': 100)])#retrieve parameters

    response = client.service.citedReferences('WOS',uid,'en', rparams)
             #tells api which database to query^         ^query language
    saveFile.write(response)

saveFile.close()#saves your output file

f.close()#closes your output file, which will appear in whatever directory you're in
