import urllib.request
import urllib.parse
from random import random


def read_file_txt():
    with open(r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day2\meizi\tag_a.txt', 'r') as file:
        result_read = file.readlines()
    return result_read


# .decode('utf-8')

def make_request(i):
    url = i
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1571838915; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1571838915',

    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def create_handler():
    handler = urllib.request.HTTPHandler()
    return handler


def create_opener(handler):
    opener = urllib.request.build_opener(handler)

    return opener


def get_response(request, opener):
    response = opener.open(request)

    return response.read()


if __name__ == '__main__':
    read_string = read_file_txt()
    # print(read_string)
    new_list = []
    somedict = {}
    for i in read_string:
        somedict[i.replace('\n','')]=None

    for x,y in somedict.items():
        new_list.append(x)


    for x in new_list:
        try:
            request = make_request(x)

            handler = create_handler()

            opener = create_opener(handler)

            content = get_response(request, opener)

            name = random() * 1000000000

            with open('./meizi/' + str(name) + '.html', 'wb') as file:
                file.write(content)
        except Exception as error:
            print(error)
            continue
