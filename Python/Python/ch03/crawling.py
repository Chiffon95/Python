import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    #print(data.content)
    return data.content

def parse(pageString):
    bs0bj = BeautifulSoup(pageString, "html.parser")
    ul = bs0bj.find("ol", {"class" : "music_list"})
    lis = ul.findAll("li", {"class" : "list_item _sap_item _svp_item"})
    ul = bs0bj.find("ol", {"class" : "music_list _more_content"})
    lis1 = ul.findAll("li", {"class" : "list_item _sap_item _svp_item"})
    print(len(lis) + len(lis1), "개")
    for i in range(0, len(lis)):
       li = lis[i]
       rank = li.find("em", {"class" : "rank"})
       rank = rank.text
       tit = li.find("a", {"class" : "tit"})
       title = tit.text
       print(rank, "위. ", title)
    for i in range(0, len(lis1)):
       li = lis1[i]
       rank = li.find("em", {"class" : "rank"})
       rank = rank.text
       tit = li.find("a", {"class" : "tit"})
       title = tit.text
       print(rank, "위. ", title)

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%AE%A4%EC%A7%81&oquery=beautifulsoup&tqi=hsFQzlprvh8ssdQTKHRsssssteo-069389"
pageString = crawl(url)
parse(pageString)