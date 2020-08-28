import requests 
from bs4 import BeautifulSoup
import hashlib
import re

req = requests.session()
url = ''

def soup_it(url):
    result = req.get(url)
    src = result.content
    clean_up = re.compile('<.*?>')
    soup = BeautifulSoup(src, "lxml")
    return re.sub(clean_up, '', str(soup))

# Get the string
output = soup_it(url)
string = output.split('string')[1]
output_string = string.rstrip()

# Encrypt string 
md5Hash = hashlib.md5(output_string.encode('utf-8')).hexdigest()

# POST it to the app
data_dump = dict(hash=md5Hash)
rpost = req.post(url=url, data=data_dump)


print(rpost.text)


