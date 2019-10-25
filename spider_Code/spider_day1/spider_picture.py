import re
import urllib.request
import urllib.parse
from random import random

file_list = []

url_list = []

with open('xiaohuawang', 'rb') as file:
    content = file.readline()
    while content:
        file_list.append(content.decode('utf-8'))
        content = file.readline()

for i in file_list:

    comp = re.compile(r'''(?<=src=").+?(?=")''')

    request =re.findall(comp,i)
    if request:

        url_list.extend(request)

print(url_list)

for urls in url_list:
    url = 'http:'+urls

    last_name = url.split('.')[-1]

    if last_name == 'jpg' or last_name == 'png':
        randomint = str(int(random() * 100000000))

        response = urllib.request.urlretrieve(url=url, filename='./picture_baidu/picture' + randomint +'.'+ last_name)
