import urllib.request
import urllib.error

url = 'http://www.baidsu.com/s?h=youarefuckedfdjak;fa'

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}

request = urllib.request.Request(url=url, headers=headers)

try:
    responsse = urllib.request.urlopen(request)
except urllib.error.HTTPError as f:
    print('http has some mistake')

except urllib.error.URLError as url:
    print('url has some mistake')
else:
    print(responsse.read().decode('utf-8'))
