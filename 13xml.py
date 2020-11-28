import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = "http://py4e-data.dr-chuck.net/comments_941123.xml"

print('Retrieving', serviceurl)

uh = urllib.request.urlopen(serviceurl)  # connect
data = uh.read()  # read

print('Retrieved', len(data), 'characters')  # check data qty

tree = ET.fromstring(data)  # create a tree

lst = tree.findall('comments/comment')  # drills down

print("Count:", len(lst))  # list length

total = sum([int(i.find('count').text) for i in lst])  # convert to int & sum

print("Sum:", total)
