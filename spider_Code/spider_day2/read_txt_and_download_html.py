import urllib.request
import urllib.parse


def read_file_txt():
    with open('D:\CodeOfPython\Code_python_normal\spider_Code\spider_day2\list.txt', 'rb') as file:
        result_read = file.readlines()
    return result_read


# .decode('utf-8')

def make_request(i):
    url = i
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
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
    for i in read_string:
        try:
            request = make_request(i.decode('utf-8'))

            handler = create_handler()

            opener = create_opener(handler)

            content = get_response(request,opener)

            name = i.decode('utf-8').rsplit('/')[-1]
            name =name.replace('.','_')
            name =name.replace('?','')
            name = name.replace('\r\n','')

            with open('./meinvtu/'+name+'.html','wb') as file :
                file.write(content)
        except Exception as error:
            print(error)
            continue
