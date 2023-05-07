# 至少应设计一个类将数据读取、接口调用或可视化等功能囊括其中。
import requests
from bs4 import BeautifulSoup as BS

class Scientist:
    def __init__(self, name):
        self.name = name
        self.dblp_url = 'https://dblp.org/search?q='+name+'&h=1000&f=0&c=1000'
        print(self.dblp_url)
    # get the scientist's articles list
    def get_articlelist(self):
        response = requests.get(self.dblp_url)
        soup = BS(response.text, 'html.parser')
        articlelist = []
        #for article in soup.select

        result_list = soup.find("ul", class_="result-list")
        if result_list:
            for li in result_list.find_all("li"):
                a_tag = li.find("a")
                if a_tag:
                    href = a_tag.get("href")
                    span_tag = a_tag.find("span", itemprop="name")
                    if span_tag:
                        name = span_tag.text
                        print(href, name)
        