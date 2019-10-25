import urllib.request
import urllib.parse


def make_request(page):
    lianjiawang_url = 'https://sh.lianjia.com/ershoufang/pg'
    url = lianjiawang_url + str(page)
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60", }
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

    for page in range(start_with, end_with + 1):
        request = make_request(page)
        response = take_response(request)

        with open('./origin_of_lianjia/lianjiawang' + str(page) + '.html', 'wb') as file:
            file.write(response.read())
