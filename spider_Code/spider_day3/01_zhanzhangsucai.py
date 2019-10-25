import re
import urllib.request
import urllib.parse


# 4
def make_request(page):
    lianjiawang_url = 'http://sc.chinaz.com/tupian/rentiyishu'
    if int(page) ==1:
        url = lianjiawang_url  + '.html'
    elif int(page) >1:
        url=lianjiawang_url  +str(page)+ '.html'
    else:
        url=lianjiawang_url + '.html'
    headers = {
        'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=Nfvu0LkOM_JhYX1tXZ2zx1lGfNmVmy_rSEFimbORXN_&wd=&eqid=c865e32700002932000000055db1127b; UM_distinctid=16dfbb049d27e2-0b68522342d2eb-b363e65-122edd-16dfbb049d360d; CNZZDATA300636=cnzz_eid%3D688632886-1571882865-null%26ntime%3D1571882865; BDTUJIAID=0ab7f1993d11ca8bae7e74da6bf78994; CNZZDATA3435928=cnzz_eid%3D1340658353-1571883056-http%253A%252F%252Fsc.chinaz.com%252F%26ntime%3D1571883056; __gads=Test',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


# https://sh.lianjia.com/ershoufang/pg3/'
#  美女网   www.meinv.hk    妹子图  反爬
#     中华英才网   智联招聘 拉钩 boos直聘
#     链家网    房天下上海二手房https://sh.esf.fang.com/house/i32/   贝壳   搜房网


def take_response(request):
    handler = urllib.request.HTTPHandler()

    switch = urllib.request.build_opener(handler)

    response = switch.open(request)

    return response


def download_picture(p, s):
    try:
        result_list = re.findall(p, s)

        for src in result_list:
            url = list(src)[0]
            name = list(src)[1] + '.jpg'
            urllib.request.urlretrieve(url=url, filename='./zhanzhangsucai_rentiyishu/' + name)
        print('1')
        return

    except:

        print('error')


if __name__ == '__main__':
    pattern = re.compile(r'<img src2="(.*?)" alt="(.*?)"')
    start_with = int(input('想要从哪一页开始？：'))
    end_with = int(input('想要到哪一页结束？：'))

    for page in range(2, end_with + 1):
        request = make_request(page)
        response = take_response(request)
        new_context = response.read().decode('utf-8')
        download_picture(pattern, new_context)
