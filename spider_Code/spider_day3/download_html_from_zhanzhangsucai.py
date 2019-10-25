import urllib.request
import urllib.parse


def make_requset(page):

    base_url= 'http://sc.chinaz.com/tupian/rentiyishu'
    lase_name ='.html'
    data={

    }

    headers={
        'Cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=Nfvu0LkOM_JhYX1tXZ2zx1lGfNmVmy_rSEFimbORXN_&wd=&eqid=c865e32700002932000000055db1127b; UM_distinctid=16dfbb049d27e2-0b68522342d2eb-b363e65-122edd-16dfbb049d360d; CNZZDATA300636=cnzz_eid%3D688632886-1571882865-null%26ntime%3D1571882865; BDTUJIAID=0ab7f1993d11ca8bae7e74da6bf78994; CNZZDATA3435928=cnzz_eid%3D1340658353-1571883056-http%253A%252F%252Fsc.chinaz.com%252F%26ntime%3D1571883056; __gads=Test',
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    url = base_url+urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url,headers=headers)
    return request