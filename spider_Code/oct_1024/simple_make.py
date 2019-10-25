import urllib.request
import urllib.parse


def get_request(url, data, headers):
    url = url + urllib.parse.urlencode(data)
    headers = headers
    request = urllib.request.Request(url=url, headers=headers)
    return request


def post_request(url, data, headers):
    url = url
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = headers
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def create_http_handler():
    handler = urllib.request.HTTPHandler()
    return handler


def create_pro_handler(proxies):
    proxies = proxies
    handler = urllib.request.ProxyHandler(proxies=proxies)
    return handler


def create_cookie_handler(cookie):
    cookie = cookie
    handler = urllib.request.HTTPCookieProcessor(cookie)
    return handler


def create_opener(handler):
    opener = urllib.request.build_opener(handler)
    return opener


def get_content_with_handler(opener, request, encoding='utf-8'):
    response = opener.open(request)
    content = response.read().decode(encoding)
    return content


def get_content_with_response(request,encoding='utf-8'):
    response = urllib.request.urlopen(request)
    content = response.read().decode(encoding)
    return content
