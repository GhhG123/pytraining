# 至少应设计一个类将数据读取、接口调用或可视化等功能囊括其中。
import requests
from bs4 import BeautifulSoup as BS

class Scientist:
    def __init__(self, name):
        self.name = name
        self.dblp_url = 'https://dblp.org/search?q={name}&h=1000&f=0&c=1000'

    # get the scientist's articles list
    def get_articlelist(self):
        response = requests.get(self.dblp_url)
        soup = BS(response.text, 'html.parser')
        articlelist = []
        #for article in soup.select
        li_tags = soup.find_all('li')
        for li in li_tags:
            span = li.find('span', class_='title')
            if span:
                title = span.text
                print(title)
            a = li.find('a')
            if a:
                link = a['href']
                print(link)