import urllib.request
import urllib.parse

lianjiawang_url ='https://sh.lianjia.com/ershoufang/l2/?utm_source=baidu&utm_medium=pinzhuan&utm_term=biaoti&utm_content=biaotimiaoshu&utm_campaign=sousuo&ljref=pc_sem_baidu_ppzq_x'

data={
'utm_source': 'baidu',
'utm_medium': 'pinzhuan',
'utm_term': 'biaoti',
'utm_content': 'biaotimiaoshu',
'utm_campaign': 'sousuo',
'ljref': 'pc_sem_baidu_ppzq_x',
}

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=lianjiawang_url,data=data,headers=headers)

handler =urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)


response = opener.open(request)


with open('lianjie_page1.html','wb') as lianjie :
    lianjie.write(response.read())














