from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

dir_name = os.path.dirname(__file__)
file_dir = os.path.join(dir_name, "todayNews\\newsHyperlinks.txt")
filename = file_dir
news_dir = os.path.join(dir_name, "todayNews\\news.txt")
with open(filename, encoding="utf8") as file_object:
  urls = file_object.readlines()
  for url in urls:
    html = urlopen(str(url))
    html_obj = bs(html.read(), 'html.parser')
    # print(html_obj)
    for i in html_obj.find_all('p'):
      txt = i.get_text()
      with open(news_dir, "a+", encoding="utf8") as file_obj:
        file_obj.write(txt + "\n")

file_content = open(news_dir, encoding='utf-8').read()
stopword = set(STOPWORDS)
stopword.update(['saying','said','think','going','seemed','will'])
wc = WordCloud( stopwords = stopword,
                background_color = 'white',
                width = 1200,
                height = 1000 ).generate(file_content)
plt.imshow(wc)
plt.axis("off")
plt.show()