import re


def open_file():
    with open('D:\CodeOfPython\Code_python_normal\spider_Code\spider_day2\meinvtu\meinvtu.html', 'rb') as file:
        data_in_file = file.read().decode('utf-8')
    return data_in_file


if __name__ == '__main__':
    data_from_file = open_file()
    patte = re.compile(r'(?<=href=").*?(?=")')

    result = re.findall(patte,data_from_file)
    for i in result:
        print(i)
        # with open('./list.txt', 'ab') as fil:
        #     fil.write(i.encode('utf-8'))
        #     fil.write(b'\r\n')


