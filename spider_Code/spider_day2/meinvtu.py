import urllib.request
import urllib.parse

#不得了的app，营养不行不要下
# http://app.nbcmwl.com/app/蜜约_美女聊天约会.apk
# http://app.nbcmwl.com/app/蜜播_美女直播.apk

def make_request(page):
    meinvtu_url = 'http://www.meinv.hk/?'

    data = {
        'cat': page,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Cookie': 'wp_xh_session_814d1d62fadab3437f112985c6990bab=90c457c5654e89108cfa2baf81f67238%7C%7C1572007614%7C%7C1572004014%7C%7C2a9444481b7b8dde3f0b6f14102e828a; UM_distinctid=16df8a7c88f1b5-0dfce5b16bc244-b363e65-122edd-16df8a7c890153; CNZZDATA1276797113=1996124286-1571833601-%7C1571833601; Hm_lvt_f1cc8ef17d832bfa40dc8354bc4dc257=1571834809; Hm_lpvt_f1cc8ef17d832bfa40dc8354bc4dc257=1571834837',
    }
    url = meinvtu_url + urllib.parse.urlencode(data)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def create_handler():
    handler = urllib.request.HTTPHandler()
    return handler


def create_opener(handler):
    opener = urllib.request.build_opener(handler)
    return opener


if __name__ == '__main__':
    start_with = int(input('来个正整数'))
    end_with = int(input('再来个正整数，比上面的大一点吧'))
    for page in range(start_with, end_with + 1):
        request = make_request(page)
        handler = create_handler()
        opener = create_opener(handler)
        response = opener.open(request)

        with open('./meinvtu/meinvtu_cat=' + str(page) + '.html', 'wb')as file:
            file.write(response.read())
