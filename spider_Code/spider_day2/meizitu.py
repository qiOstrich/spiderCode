import urllib.request
import urllib.parse

url = 'https://www.mzitu.com/tag/youhuo/?ivk_sa=1023231z'


def make_request():
    # data = {
    #     'ivk_sa': '1023231z',
    # }

    headers = {
        'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1571838915; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1571838915',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    newurl = url
    request = urllib.request.Request(headers=headers, url=newurl)

    return request


def make_handler():
    handler = urllib.request.HTTPHandler()

    return handler


def make_opener(handler):
    opener = urllib.request.build_opener(handler)
    return opener


def get_response(opener, request):
    response = opener.open(request)
    return response.read()


if __name__ == '__main__':
    request = make_request()

    handler = make_handler()

    opener = make_opener(handler)
    content = get_response(opener, request)

    with open('./meizi/home.html', 'wb')as file:
        file.write(content)
