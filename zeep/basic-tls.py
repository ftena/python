import zeep

wsdl = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'
client = zeep.Client(wsdl=wsdl)

# Call the service method
response = client.service.NumberToWords(123)
print(response)  # Output: "one hundred and twenty-three"
