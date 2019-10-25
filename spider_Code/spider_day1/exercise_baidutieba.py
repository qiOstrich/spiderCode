import urllib.request
import urllib.parse

# https://tieba.baidu.com/f?ie=utf-8&kw=%E5%89%91%E6%9D%A5&fr=search

# ie: utf-8
# kw: 剑来
# fr: search
url = 'https://tieba.baidu.com/f?'

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    'Cookie': 'Hm_lvt_1039f1218e57655b6677f30913227148=1571742307; Hm_lpvt_1039f1218e57655b6677f30913227148=1571742307; ASP.NET_SessionId=buc2sq3rnkhmol03glt4a1tp; KLBRSID=a34b6eb1eda6f7a05724ede2e440cdc7|1571742352|1571742307',
}

data = {
    'ie': 'utf-8',
    'kw': '剑来',
    'fr': 'search',
}

kw = input('请输入需要搜索的贴吧:')

if kw:
    data['kw'] = str(kw)

url_now = url + urllib.parse.urlencode(data)

request = urllib.request.Request(url=url_now, headers=headers)

response = urllib.request.urlopen(request)

spider = response.readlines()

with open('../oct_1024/tieba_search' + kw + '.html', 'wb')as file:
    for i in spider:
        file.write(i)
