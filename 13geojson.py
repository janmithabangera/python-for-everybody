import ssl
import urllib.request, urllib.parse, urllib.error
import json

api_key= False
# api_key='....'
if api_key is False:
    api_key=42
    serviceurl= 'http://py4e-data.dr-chuck.net/json?'

else:
    serviceurl='https://maps.googleapis.com/maps/api/geocode/json?'

## Ignore SSL certification
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    address= input('Enter Adderss: ')
    if len(address)< 1: break

    contents= dict()
    contents['address']=address
    if api_key is not False: contents['key']=api_key
    url= serviceurl+ urllib.parse.urlencode(contents)

    print('Retrieving:', url)
    access= urllib.request.urlopen(url, context=ctx)
    data= access.read().decode()
    print('Retrieved', len(data), 'characters')

    ## check--- working or not
    try:
        js= json.loads(data)
    except:
        None

    # check if status is OK
    if not js or 'status' not in js or js['status'] != 'OK':
        print('========Failure To Retrieve=========')
        print(data)
        continue

    ## For proper representation
    print(json.dumps(js, indent=4))
    ## Print various values
    loc= js['results'][0]['place_id']
    print('Loc', loc)
    addr= js['results'][0]['formatted_address']
    print('Address of', address,'is:',addr)
    lati= js['results'][0]['geometry']['location']['lat']
    long= js['results'][0]['geometry']['location']['lng']
    print('Latitude:',lati,'\nLongitude:',long)
