from suds.client import Client
from time import sleep
import csv

a_url = 'http://search.webofknowledge.com/esti/wokmws/ws/WOKMWSAuthenticate?wsdl'
a_client = Client(a_url)
a_client.set_options(headers={'Authorization':'Basic '})
                                                    #^base10 encoded username and pw goes here 
ID = a_client.service.authenticate()
SID = 'SID='
SID += ID

f = open('yourcsv.csv')#csv with list of wos accession numbers

csv_f = csv.reader(f)

saveFile = open('citations.xml','ab')#creates new xml file and appends each reference list to the file

for uid in csv_f:
    sleep(0.6)
    url = 'http://search.webofknowledge.com/esti/wokmws/ws/WokSearch?wsdl'
    client = Client(url, retxml=True)
    client.set_options(headers={'Content-type':'text/xml', 'Cookie': SID})

    rparams = {'firstRecord' : 1, 'count': 100}

    response = client.service.citedReferences('WOS',uid,'en', rparams)

    saveFile.write(response)

saveFile.close()

f.close()

#see comments in WOK_citedRef_loop.py for more detailed comments

