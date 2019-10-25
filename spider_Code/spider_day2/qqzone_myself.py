import urllib.request
import urllib.parse

myqqurl = 'https://h5.qzone.qq.com/lookup/video/vwecam.gtimg.com/1006_940a1df63e0b4b3ab08d36f52349ccbb.f0.mp4?'
data = {
    'ptype': ' http',
    'vkey': ' 02AF3C8F8CB0EBB2B81E92F544954CC1A1E58660ED4B7950DF721F9DE10A684F50E43E07AFBC0AAA497BBEC9F1C46BDD8DDDF4DF2E1D5CAF',
    'sdtfrom': ' v1000',
    'owner': ' 951850464',
    'qzonetoken': ' 780a9b0f893520f758724fe0b59231cea4658edea1e05bdfed774b02666fe21f2cd8119e852e26f5',
    'g_tk': ' 960795971',
}

# ADUIN: 951850464
# ADSESSION: 1571831557
# ADTAG: CLIENT.QQ.5659_MyTip.0
# ADPUBNO: 26941
# source: namecardhoverstar


formdata = {
    'list': ' 0',
    'outputType': ' fs',
    'qzreferrer': ' https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds_html_module?g_iframeUser=1&i_uin=951850464&i_login_uin=951850464&mode=4&previewV8=1&style=1&version=8&needDelOpr=true&transparence=true&hideExtend=false&showcount=5&MORE_FEEDS_CGI=http%3A%2F%2Fic2.s12.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_act_all&refer=2&paramstring=os-winxp|100',
}
formdata = urllib.parse.urlencode(formdata).encode('utf-8')
data = urllib.parse.urlencode(data)
headers = {
    'Content-Type': ' application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': ' https://user.qzone.qq.com',
    'Referer': 'https://user.qzone.qq.com/951850464?ADUIN=951850464&ADSESSION=1571831557&ADTAG=CLIENT.QQ.5659_MyTip.0&ADPUBNO=26941&source=namecardhoverstar',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',

}

request = urllib.request.Request(url=myqqurl + data, data=formdata, headers=headers)

handler = urllib.request.HTTPHandler()

myopener = urllib.request.build_opener(handler)

response = myopener.open(request)
with open('./qqzone/951850464qqzone.json', 'wb')as file:
    file.write(response.read())
