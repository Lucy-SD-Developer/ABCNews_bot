from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve #导入urlretrieve函数，用于下载图片
import os

dir_name = os.path.dirname(__file__)
file_dir = os.path.join(dir_name, "todayNews")
if os.path.exists(file_dir) == False:
    os.makedirs(file_dir)

html = urlopen("https://abcnews.go.com/")
html_obj = bf(html.read(), 'html.parser')

for s in html_obj.find_all('span'):
    s.extract()
news_info = html_obj.find_all('div', class_="headlines-li-div")

filename = os.path.join(file_dir, "newsHeadlines.txt")
for n in news_info:
    print(n.text.strip() + "\n")
    with open(filename, "a+") as file_obj:
        file_obj.write(n.text.strip())
        file_obj.write("\n")
        file_obj.write("\n")