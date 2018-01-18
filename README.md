# WOKapiscripts: a repository of python scripts for interacting with the Web of Science Web Services Premium API. 

### Intro

These Python scripts interact with Web of Science Web Services Premium aka Web of Science API. I named this repository when Thomson Reuters (now Clarivate) was calling it Web of Knowledge, hence WOKapiscripts. Now it's back to WOS but I don't want to change my url.

The purpose of this project was to download cited reference data en masse for a citation analysis I've been working on. Lately I've been adding a few more scripts to accomplish different things. Each of these scripts perform discrete tasks. In other words, each script does one thing. As I continue writing scripts to extract other information from the WOS API, I'll add them here.

-Phil

University of Colorado Boulder Libraries
philip.white@colorado.edu

### Links

[Documentation for WOS Web Services Premium](http://ipscience-help.thomsonreuters.com/wosWebServicesExpanded/WebServicesExpandedOverviewGroup/Introduction.html)

[Read about WokSearch Operations & search parameters](http://ipscience-help.thomsonreuters.com/wosWebServicesExpanded/WebServiceOperationsGroup/WSPremiumOperations.html)

[WOS Field Tags for a User Query](http://ipscience-help.thomsonreuters.com/wosWebServicesExpanded/WebServiceOperationsGroup/WSPremiumOperations/wokSearchGroup/search/user_query/fieldTagsGroup/WOSfieldTags.html)

[WOS Field Names](http://ipscience-help.thomsonreuters.com/wosWebServicesExpanded/appendix1Group/wosfieldNameTable.html)

[Information about SOAP APIs](https://www.w3schools.com/xml/xml_soap.asp)

[Python](https://www.python.org/)

[Python module SUDS](https://bitbucket.org/jurko/suds/wiki/Original%20Documentation)

### You should Read This Before Attempting To Use

- Your institution must have a subscription to Web Services Expanded.
- The WOS API is a SOAP API --learn how SOAP works.
- Review the Web of Science Web Services Expanded documentation thoroughly before using this script.
- Review SUDS documentation and examples: https://bitbucket.org/jurko/suds/wiki/Original%20Documentation 
- Learn how to use SUDS.
- I used suds-jurko 0.6. Other suds packages threw errors.
- The authentication request must contain institutional username and password encoded into Base64 as a header as well as SOAP envelope in xml with authentication parameters.
- When done correctly, you'll recieve an xml message in return with session ID (SID), which is a parameter for subsequent requests.
- Review the WOS authentication docs & the request docs.
- These scripts are throttled to a 0.6 second interval between requests to comply with the terms of use.
 
### Scripts

#### WOK_citedRef_loop.py
This script opens a csv containing a list of WOS accession numbers, loops those accession numbers into individual SOAP requests, and appends the response of each request into a new txt file. The content of that txt file will be in xml. This script is heavily commented and explains fairly well what is happening and what information users need to plug in. It's worth reviewing just for those comments. Note this script does not include the authentication step; it requires authentication separately, which is explained in the comments.

#### WOK_authent_citedRef_loop.py
Same as above script with the authentication process added in. 

#### WOK_doiSearch_loop.py
Queries the WOS API for information about articles identified by their DOIs. Same principle as the above scripts; feeds a list of DOIs into individual SOAP requests. Then performs a userQuery for each DOI, returning data for each DOI of the specified fields. In this case, the fields are 'name' 'title' 'abstract'. See field names link above for other options. 

### Attribution
Please acknowledge and cite your use of the scripts available in this repository.

Suggested citation: White, P.B. (2017). WOKapiscripts. GitHub Repository. https://github.com/outpw/WOKapiscripts
