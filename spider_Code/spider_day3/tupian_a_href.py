import urllib.request

zhanzhangsucai_url = 'http://sc.chinaz.com/tupian/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

request = urllib.request.Request(url=zhanzhangsucai_url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

from lxml import etree

tree = etree.HTML(content)

keys = tree.xpath('//div[@class="right"]//a[@target="_blank"]/@href')
values = tree.xpath('//div[@class="right"]//a[@target="_blank"]/text()')

with open('./link_a_from_zhanzhang/a_link.txt', 'wb') as file:
    for count in range(0, len(keys)):
        file.write(keys[count].encode('utf-8') + ':'.encode('utf-8') + values[count].encode('utf-8'))
        file.write(b'\n')
