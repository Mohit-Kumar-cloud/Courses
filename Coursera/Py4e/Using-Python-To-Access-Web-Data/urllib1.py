from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_860111.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count=0
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
     sum+=int(tag.contents[0])
     count+=1
print("Sum:",sum)     
print("Count:",count)