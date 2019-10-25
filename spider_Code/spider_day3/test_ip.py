import random
import urllib.request
import urllib.parse

url = 'https://www.baid.com/s?wd=ip'

url = url
headers = {
    'Cookie': 'BIDUPSID=69D237F1CA4BC3D97BBCDC5EE3DFDE2D; BAIDUID=67EE0402DD723F80CF4223CB11D286D6:FG=1; PSTM=1568442553; BD_UPN=12314753; BDUSS=JSenlHSmZId3ctZjVaNU84aEg5ZnNkd0taQmNyd3RMUzU0eFAtY0VLT29kYWhkRVFBQUFBJCQAAAAAAAAAAAEAAADJQ3wYxuvD98~pMjQxMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKjogF2o6IBdcE; MCITY=-289%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1425_21101_29920_29567_29221_26350; delPer=0; BD_CK_SAM=1; PSINO=3; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; shifen[133904269319_31846]=1571916331; shifen[139247814470_6340]=1571916368; BCLID=10468160672912024281; BDSFRCVID=JxKOJeC62RlRJm5w48btJF3pG_nGBsOTH6aocg7IbqGkf-hCTDFnEG0P_f8g0KAbIVlyogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oIDaJCv5j5r1MtQ_M4F_qxby26nb3HReaJ5n0-nnhpbsLpQbj5QbWt8t0xKHfCnI54D5LIQmjnIRy6CajTcLeaDeqbbfb-oh3RrjHJOoDDv2eq35y4LdLp7xJ-IJaDrf_njeLRF-KDobyP56eM_hW4tH3fPeWJLH_KLbfIIMhCv65nt_2JLHhMrK2tcjHD7XV-JwXh7keq8CD6jj0R0E-ltJqIrfWeFeQp325quWVDQ2y5jHhPKp5UFDhfvBfG7vbJnatRbpsIJMybAWbT8U5f5MJnkqaKviaKJHBMb1jpODBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jbDH0DqT-efKbe0n48bn6bfnPk-PnVeUIbyPnZKxtqtHrQbqcEJ40MbbomyxD5KM-mh4JGbMRnWncKWbOjJhTDqq3cbCcsLp0vQxT405OTXKFO0KJc0RozSRRwhPJvyT88XnO7aMJlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKC5bD-mefK; H_PS_645EC=4f59I5ZfcJaqlwmBLr3JH74iBAoR3ZiVBo%2BC5wu%2FN5JJ2wbIaHJ3432gSCIBlk7EQ9OW; BDSVRTM=114; COOKIE_SESSION=151_2_7_4_4_8_0_0_4_5_19_1_0_0_25_1_1571916391_1571916367_1571916517%7C9%2337_27_1571916366%7C9; WWW_ST=1571916711041',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.1',
}

request = urllib.request.Request(url=url, headers=headers)

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
]
for i in ip_list:

    proxies = i
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    try:
        response = opener.open(request)
        print('this will pass :  ' + str(i))
    except:
        print('no :  ' + str(i))
