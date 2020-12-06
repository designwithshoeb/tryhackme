


# Emdee Five For Life - 26/11/2020
import requests
import hashlib
import re
# IP address of instance.
url="http://178.128.40.63:30323/"
rs= requests.session()
r=rs.get(url)
print(r.text)
ot=re.search("<h3 align='center'>.*</h3>",r.text)
ot=re.search(">.*<",ot[0])
ot=ot[0]
print(ot)
ot=ot[1:-1]
ot=hashlib.md5(ot.encode('utf-8')).hexdigest()
print(ot)
data={'hash':ot}
ot=rs.post(url=url,data=data)
print(ot.text)



	
	
