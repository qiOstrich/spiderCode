import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&limit=20&start='

start = input('请输入起始页码：')
end = input('请输入结束页码：')

for page in range(int(start), int(end) + 1):
    url_now = url + str(page)
    response = urllib.request.urlopen(url_now)
    with open('../douban/response' + str(page) + '_move.md', 'w')as file:
        file.write(response.read().decode('utf-8'))

# url = url + '1'
# response = urllib.request.urlopen(url)
# with open('response' + '1' + '_move.md', 'w')as file:
#     file.write(response.read().decode('utf-8'))
