from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve #导入urlretrieve函数，用于下载图片

html = urlopen("https://abcnews.go.com/")
html_obj = bf(html.read(), 'html.parser')
img_info = html_obj.find_all('img')
print(img_info)

for i in img_info:
    img_url = i.get('data-src', None)
    print(img_url)
    if img_url is None: #无这行则报错，试试看没有的情况再debug：TypeError: expected string or bytes-like object 碰到第一个没有url的就报错了
        continue
    urlretrieve(img_url, "K:\\myCrawler\\newsPicture\\news" + str(img_info.index(i)) + '.jpg')