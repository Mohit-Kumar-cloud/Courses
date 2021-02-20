import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Asra.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
pos=int(input("Enter Position:"))-1
rep=int(input("Enter Repeat count:"))
print(url)
for i in range(rep):
    tags = soup('a')
    print(tags[pos].get('href',None))
    url1 = tags[pos].get('href',None)
    html1 = urllib.request.urlopen(url1, context=ctx).read()
    soup = BeautifulSoup(html1, 'html.parser')
    
