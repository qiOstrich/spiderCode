import urllib.request
import urllib.parse

#did not make it

def make_request(page):
    lianjiawang_url = 'https://sh.esf.fang.com/house/i3'
    url = lianjiawang_url +str(page)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': ' max-age=0',
        'cookie': 'city=sh; global_cookie=hg34gjz44m5jqc6rbkvzfl0rk17k236bteg; logGuid=5d1578bd-a1a9-4ade-a0c6-71ffed5af393; g_sourcepage=ehlist; Integrateactivity=notincludemc; __utma=147393320.1576694079.1571828896.1571828896.1571828896.1; __utmc=147393320; __utmz=147393320.1571828896.1.1.utmcsr=sh.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; unique_cookie=U_hg34gjz44m5jqc6rbkvzfl0rk17k236bteg*15; __utmb=147393320.39.10.1571828896',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
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



if __name__ == '__main__':

    start_with = int(input('想要从哪一页开始？：'))
    end_with = int(input('想要到哪一页结束？：'))

    if end_with == 1:

        request = make_request(1)
        response = take_response(request)
        print(response.read())

    elif  end_with > 1:
        for page in range(2, end_with + 1):
            request = make_request(page)
            response = take_response(request)

            with open('./origin_of_fangtianxia/fangtianxia' + str(page) + '.html', 'wb') as file:
                content =response.read().decode('gb2312')

                file.write(content.encode('utf-8'))
    else:
        print('请从正整数开始')
