# https://fe-api.zhaopin.com/c/i/sou?
'''

'''
import urllib.request
import urllib.parse


def make_request(page):
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?'
    data = {
        'start': str((page - 1) * 90),
        'pageSize': '90',
        'cityId': '538',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kw': 'Python',
        'kt': '3',
        '_v': '0.51167152',
        'x-zp-page-request-id': '494b94bfe4fb48e995316a433449660c-1571906594400-829668',
        'x-zp-client-id': 'f8c05c99-c1c2-4c49-8a47-fc9ec48fc9f1',

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }

    url = base_url + urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def create_handler():
    handler = urllib.request.HTTPHandler()
    return handler


def create_opener(handler):
    opener = urllib.request.build_opener(handler)

    return opener


if __name__ == '__main__':
    start_with = int(input('起始页码'))
    end_with = int(input('结束页码'))
    if end_with > 12:
        for page in range(start_with, 13):
            request = make_request(page)
            handler = create_handler()

            opener = create_opener(handler)
            response = opener.open(request)
            content = response.read()

            with open('./zhilianzhaopian_json/shanghai_'+str(page)+'.json','wb')as file:
                file.write(content)
    else:
        for page in range(start_with, end_with+1):
            request = make_request(page)
            handler = create_handler()

            opener = create_opener(handler)
            response = opener.open(request)
            content = response.read()

            with open('./zhilianzhaopian_json/shanghai_'+str(page)+'.json','wb')as file:
                file.write(content)
