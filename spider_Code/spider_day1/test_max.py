import urllib.request
import urllib.parse


#测试请求参数中页码超过kfc原有页码返回的值

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    'Cookie': 'Hm_lvt_1039f1218e57655b6677f30913227148=1571742307; Hm_lpvt_1039f1218e57655b6677f30913227148=1571742307; ASP.NET_SessionId=buc2sq3rnkhmol03glt4a1tp; KLBRSID=a34b6eb1eda6f7a05724ede2e440cdc7|1571742352|1571742307',
}
data = {
    'cname': '上海',
    'pid': '',
    'pageIndex': '45',
    'pageSize': '10',
}

data_now = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, headers=headers, data=data_now)

response = urllib.request.urlopen(request)
json_table = response.read().decode('utf-8')

json_table = eval(json_table)

print(type(json_table))
print(json_table['Table1'])
