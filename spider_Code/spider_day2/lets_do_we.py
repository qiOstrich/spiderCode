import re

with open(r'D:\CodeOfPython\Code_python_normal\spider_Code\spider_day2\meizi\25921934.445795935.html', 'rb') as file:
    html = file.read()
# print(html.decode('utf-8'))


patt1 = re.compile(r'<a.*?/>')
patt2 = re.compile(r'(?<=href=").*?(?=")')
result1 = re.findall(patt1, html.decode('utf-8'))
result2 = []
for i in result1:
    # print(i)

    i_get = re.search(patt2, i)
    result2.append(i_get.group())

print(result2)