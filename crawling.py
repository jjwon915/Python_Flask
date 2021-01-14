# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

def daum_news():

    # https://news.daum.net/ranking/popular 에서 뉴스 랭킹 목록 가져오기 위함.
    req = requests.get("https://news.daum.net/ranking/popular")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_daum = []

    for i in soup.select("#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong"):
        list_daum.append(i.find("a").text)

    return list_daum

# 오늘의 유머
def today():
    req = requests.get("http://www.todayhumor.co.kr/board/list.php?table=bestofbest")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_today = []

    for i in soup.find_all("td", class_="subject") :
        list_today.append(i.text)

    return list_today

# OKKY
def okky():
    req = requests.get("https://okky.kr/articles/tips")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_okky = []

    for i in soup.select("#list-article > div.panel.panel-default > ul > li > div.list-title-wrapper.clearfix > h5"):
        list_okky.append(i.find("a").text)

    return list_okky
