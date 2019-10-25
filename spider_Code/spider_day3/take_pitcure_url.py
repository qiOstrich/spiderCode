import os
import random
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


def create_Phandler():
    ip_list = [
        {'https': '61.128.208.94:3128'},
        {'https': '182.88.5.99:9797'},
        {'https': '210.26.49.88:3128'},
        {'https': '218.22.7.62:53281'},
        {'https': '122.136.212.132:53281'},
        {'https': '112.250.107.37:53281'},
        {'https': '59.38.60.105:9797'},

        {'http': '183.129.207.90:31330'},
        {'http': '119.131.88.242:9797'},
        {'http': '110.16.80.106:8080'},
        {'http': '14.20.235.180:808'},
        {'http': '115.171.203.117:9000'},

    ]
    proxiex = random.choice(ip_list)
    handler = urllib.request.ProxyHandler(proxies=proxiex)
    return handler


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
    path = r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day3\link_a_from_zhanzhang\a_link.txt'
    result_list = read_file(path)
    base_url = result_list[0].rsplit(':', 1)[0]
    base_name = result_list[0].rsplit(':', 1)[1]
    # 获取当前文件的文件夹路径
    root_dir = os.path.dirname(os.path.abspath(__file__))
    #创建一个文件夹
    # os.mkdir(os.path.join(root_dir, str('root_html')))
    this_dir = os.path.join(root_dir, 'root_html')

    '''it_is_name = result_list[1].split(':')[1]

       with open(os.path.join(this_dir, it_is_name), 'wb') as file:
           file.write('i'.encode('utf-8'))
           print('ok')'''
    for index in range(1, len(result_list)):
        use_url = base_url + result_list[index].split(':')[0]
        t_is_name = result_list[index].split(':')[1][:-1]

        request = make_request(use_url)
        handler = crete_mhandler()
        opener = create_opener(handler)
        content = get_content(opener=opener, request=request)
        tree = etree.HTML(content)
        img_list = tree.xpath("//div[@id='container']//p/a[@target='_blank']/@href")
        alt_list = tree.xpath("//div[@id='container']//p/a[@target='_blank']/@alt")
        with open(os.path.join(this_dir, t_is_name), 'wb') as file:
            for count in range(len(img_list)):
                file.write(img_list[count].encode('utf-8'))
                file.write(':'.encode('utf-8'))
                file.write(alt_list[count].encode('utf-8'))
                file.write(b'\n')

    # 取第一个路由进行拼接，并取得对应网页的名字
    # use_url = base_url + result_list[1].split(':')[0]
    # it_is_name = result_list[1].split(':')[1]
    # request = make_request(use_url)
    # handler = crete_mhandler()
    # opener = create_opener(handler)
    # content = get_content(opener=opener, request=request)
    # # print(content)
    # tree = etree.HTML(content)
    # img_list = tree.xpath("//div[@id='container']//p/a[@target='_blank']/@href")
    # alt_list = tree.xpath("//div[@id='container']//p/a[@target='_blank']/@alt")
    # print(img_list)
    # print(len(img_list))
    # print(alt_list)
    # print(len(alt_list))
