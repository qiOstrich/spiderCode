import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    'Cookie': 'Hm_lvt_1039f1218e57655b6677f30913227148=1571742307; Hm_lpvt_1039f1218e57655b6677f30913227148=1571742307; ASP.NET_SessionId=buc2sq3rnkhmol03glt4a1tp; KLBRSID=a34b6eb1eda6f7a05724ede2e440cdc7|1571742352|1571742307',
}
data = {
    'cname': '上海',
    'pid': '',
    'pageIndex': '2',
    'pageSize': '10',
}

start = input('请输入起始页面')
end = input('请输入结束页面')

for page in range(int(start), int(end) + 1):
    data['pageIndex'] = str(page)
    data_now = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=url, headers=headers, data=data_now)

    response = urllib.request.urlopen(request)

    with open('../kfc_post/kfc_address_shanghai' + str(page) + '.md', 'w')as file:
        file.write(response.read().decode('utf-8'))
