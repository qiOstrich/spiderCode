import os
import urllib.request
import urllib.parse

from lxml import etree


def read_file(path):
    with open(path, 'rb') as file:
        a_list = file.readlines()
    tag_a_list = []
    for index in a_list:
        tag_a_list.append(index.decode('utf-8'))
    return tag_a_list


def make_request(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36', }
    # data = urllib.parse.urlencode(data)
    url = url
    request = urllib.request.Request(url=url, headers=headers)
    return request


def crete_mhandler():
    handler = urllib.request.HTTPHandler()
    return handler


def create_opener(handler):
    opener = urllib.request.build_opener(handler)
    return opener


def get_content(opener, request, coding='utf-8'):
    response = opener.open(request)
    content = response.read().decode(coding)
    return content


if __name__ == '__main__':
    # 创建一个文件夹，用于存储图片路径
    # os.mkdir('./picture_url/')
    base_file = read_file(
        r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day3\link_a_from_zhanzhang\a_link.txt')
    with open('./picture_url/src_alt.txt','wb')as file:
        for index in range(1, len(base_file)):
            name = base_file[index].rsplit(':', 1)[1][:-1]

            file_base = r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day3\root_html'
            result = read_file(os.path.join(file_base, name))
            # print(name)
            # print(result)

            for count in range(len(result)):
                try:
                    request = make_request(result[count].rsplit(':',1)[0])
                    handler = crete_mhandler()
                    opener = create_opener(handler)
                    content = get_content(opener=opener,request=request)
                    tree = etree.HTML(content)
                    picture_src =tree.xpath("//div[@class='imga']//img/@src")[0]
                    picture_name =tree.xpath("//div[@class='imga']//img/@alt")[0]
                    file.write(picture_name.encode('utf-8'))
                    file.write(':'.encode('utf-8'))
                    file.write(picture_src.encode('utf-8'))
                    file.write(b'\n')
                except:
                    print("Did't find, "+result[count].rsplit(':', 1)[0],result[count].rsplit(':', 1)[1][:-1])

                    continue
