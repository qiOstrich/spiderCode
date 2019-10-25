import urllib.request

url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1571725632&di=cdf6263737d8bf043c38b3ab5a34d7e8&src=http://img.ph.126.net/sMszbZPhBkh1nByh0IhNbA==/923237923611465663.jpg'

urllib.request.urlretrieve(url=url, filename='a_picture.jpg')
