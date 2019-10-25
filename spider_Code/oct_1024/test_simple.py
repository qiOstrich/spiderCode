from oct_1024.simple_make import *

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    }
    date = {
        'wd': '剑来',
    }
    request = get_request(url=url, data=date, headers=headers)
    content = get_content_with_response(request)

    print(content)
