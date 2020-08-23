from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
from urllib.request import urlretrieve #导入urlretrieve函数，用于下载图片
import os

#When a module is loaded from a file in Python, __file__ is set to its path. 
#Both dirname() and basename() only split the passed filename into components without taking into account the current directory.
dir_name = os.path.dirname(__file__)
file_dir = os.path.join(dir_name, "todayNews\\pictures")
if not os.path.exists(file_dir): #os.path.exists(file_dir) == False:
    os.makedirs(file_dir)
print(dir_name)
print(file_dir)
#To get the dirname of the absolute path, use:
print(os.path.dirname(os.path.abspath(__file__)))

html = urlopen("https://abcnews.go.com/")
html_obj = bf(html.read(), 'html.parser')
img_info = html_obj.find_all('img')
print(img_info) #return a list

for i in img_info:
    img_url = i.get('data-src', None)
    print(img_url)
    if img_url is None: 
        continue
    urlretrieve(img_url, os.path.join(file_dir, str(img_info.index(i)) + '.jpg'))
