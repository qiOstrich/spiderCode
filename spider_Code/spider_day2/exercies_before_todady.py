import urllib.request
import urllib.parse

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60"
}


def make_request(page):
    url = 'https://movie.douban.com/j/chart/top_list?'

    data = {
        'type': '13',
        'interval_id': '100 % 3A90',
        'limit': '20',
        'start': str(page),
    }


    data = urllib.parse.urlencode(data)
    url = url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request


# start = input('请输入起始页码：')
# end = input('请输入结束页码：')
# for page in range(int(start), int(end) + 1):
#     url_now = url + str(page)
#     response = urllib.request.urlopen(url_now)
#     with open('./douban/response' + str(page) + '_move.md', 'w')as file:
#         file.write(response.read().decode('utf-8'))


if __name__ == '__main__':

    start = int(input('请输入起始页码：'))
    end = int(input('请输入结束页码：'))
    for page in range(start, end + 1):
        make_request(page)

# url = url + '1'
# response = urllib.request.urlopen(url)
# with open('response' + '1' + '_move.md', 'w')as file:
#     file.write(response.read().decode('utf-8'))
