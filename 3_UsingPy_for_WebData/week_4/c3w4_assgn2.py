from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

for i in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    taglist = list()
    for tag in tags:
        taglist.append(tag.contents[0])
        if len(taglist) == 18:
            url = 'http://py4e-data.dr-chuck.net/known_by_' + taglist[-1] + '.html'
            break

print(taglist[-1])
