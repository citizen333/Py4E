from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
xmlString = urlopen(url).read()
tree = ET.fromstring(xmlString)
counts = tree.findall('.//count')
finalSum = 0
for count in counts:
    finalSum += int(count.text)
print(finalSum)