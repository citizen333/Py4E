from urllib.request import urlopen
import json

url = input('Enter - ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
jsonString = urlopen(url).read().decode()
info = json.loads(jsonString)
print('User count:', len(info['comments']))

finalSum = 0
for item in info['comments']:
    finalSum += int(item['count'])
print(type(jsonString))