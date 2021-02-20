import urllib.request,urllib.parse,urllib.error
import json
import ssl


#ignore SSL Certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE
url='http://py4e-data.dr-chuck.net/comments_860114.json'

uh=urllib.request.urlopen(url,context=ctx)
data = uh.read()
info = json.loads(data)
print('Info count:', len(info))

#print(json.dumps(info,indent=2))
sum=0
for c in info['comments']:
    sum+=int(c['count'])

print(sum)