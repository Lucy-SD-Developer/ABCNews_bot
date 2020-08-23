from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve #导入urlretrieve函数，用于下载图片
import os

dir_name = os.path.dirname(__file__)
file_dir = os.path.join(dir_name, "todayNews")
if not os.path.exists(file_dir): #os.path.exists(file_dir) == False:
    os.makedirs(file_dir)

html = urlopen("https://abcnews.go.com/")
html_obj = bs(html.read(), 'html.parser')

for s in html_obj.find_all('span'):
    s.extract()
news_info = html_obj.find_all('div', class_="headlines-li-div") #return a list

filename = "todayNewsHeadline.txt"
for n in news_info:
    print(n.text.strip() + "\n")
    with open(filename, "a+") as file_obj:
        file_obj.write(n.text.strip()+"\n"+"\n")

filename = os.path.join(file_dir, "newsHyperlinks.txt")
for h in news_info:
  print(h.a.get('href'))
  with open(filename, "a+") as file_obj:
    if (str(h.a.get('href')) != "javascript:void(0);"):
      file_obj.write(str(h.a.get('href')))
      file_obj.write("\n")
