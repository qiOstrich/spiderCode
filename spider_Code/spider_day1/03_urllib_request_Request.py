import urllib.request

url = 'http://www.baidu.com'

#更改ua可以百度ua大全，随便哪一个都能用
headers ={
"User_Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}

request = urllib.request.Request(url=url,headers=headers)

response =urllib.request.urlopen(request)

print(response.read().decode('utf-8'))

