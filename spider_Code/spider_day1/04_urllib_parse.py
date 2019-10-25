import urllib.request
import urllib.parse


#默认这样会发送post请求
url = 'http://www.baidu.com/s?'

data = {
    'wd': '养成系'
}

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
