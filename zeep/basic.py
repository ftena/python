import zeep

# the URL for the SOAP service
wsdl = 'https://www.soapclient.com/xml/soapresponder.wsdl'

# create client
client = zeep.Client(wsdl=wsdl)

print(client.service.Method1('Zeep', 'is cool'))


