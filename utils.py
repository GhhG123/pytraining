# 至少应设计一个类将数据读取、接口调用或可视化等功能囊括其中。
import requests
from bs4 import BeautifulSoup as BS

class Scientist:
    def __init__(self, name):
        #self.name = input('Please input the name of the scientist: ')
        self.name = name
        new_name = self.name.replace(' ', '+')
        self.dblp_url = 'https://dblp.org/search?q='+new_name+'&h=1000&f=0&c=1000'
        print(self.dblp_url)
    # get the scientist's articles list
    def get_scientist_link(self):
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
                        if name==self.name:
                            print(href, name)
                            return href
                        
    #get the article list
    def get_articlelist(self,link):
        response = requests.get(link)
        soup = BS(response.text, 'html.parser')
        articlelist = []
        title_spans = soup.select('span.title[itemprop="name"]')

        # 
        for title_span in title_spans:
            title = title_span.text
            print(title)
            next_a = title_span.find_next_sibling('a')
            if next_a is not None:
                href = next_a.get('href')
                print(href)
                articlelist.append({'title': title, 'link': href})
        return articlelist

        