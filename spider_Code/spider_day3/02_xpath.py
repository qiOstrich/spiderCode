import urllib.request

url = 'http://sc.chinaz.com/tag_tupian/OuMeiMeiNv.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

context = response.read().decode('utf-8')

from lxml import etree

tree = etree.HTML(context)

src_list = tree.xpath('//a[@target="_blank"]/img/@src2')
alt_list = tree.xpath('//a[@target="_blank"]/img/@alt')

for count in range(0, len(src_list)):
    new_url = src_list[count]
    sufix = src_list[count].split('.')[-1]
    filename = './oumeidabo/' + alt_list[count] + '.'+sufix
    urllib.request.urlretrieve(url=new_url, filename=filename)
