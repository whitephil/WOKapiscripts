from suds.client import Client
from time import sleep
import csv

a_url = 'http://search.webofknowledge.com/esti/wokmws/ws/WOKMWSAuthenticate?wsdl'
a_client = Client(a_url)
a_client.set_options(headers={'Authorization':''})
           #encoded log in credentials go here^
ID = a_client.service.authenticate()
SID = 'SID='
SID += ID

f = open('doi.csv')

csv_f = csv.reader(f)

saveFile = open('data.xml','ab')

for doi in csv_f:
    sleep(0.6)
    url = 'http://search.webofknowledge.com/esti/wokmws/ws/WokSearch?wsdl'
    client = Client(url, retxml=True)
    client.set_options(headers={'Content-type':'text/xml', 'Cookie':SID})

    qparams = {'databaseId':'WOS', 'userQuery':doi,'queryLanguage':'en'}

    fields={'collectionName':'WOS','fieldName':'name','fieldName':'title','fieldName':'abstract'}

    rparams={
        'firstRecord' : 1,
        'count': 100,
        'viewField' : fields
        }

    response = client.service.search(qparams, rparams)

    saveFile.write(response)

saveFile.close()

f.close()
