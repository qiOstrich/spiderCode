import urllib.request
import urllib.parse

url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE%CD%BC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"

}

data = {

}

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

result = response.readlines()

with open('newfile.txt','ab') as fileme:
    for res in result:
        fileme.write(res)
