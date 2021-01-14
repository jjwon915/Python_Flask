# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

def daum_news():

    # https://news.daum.net/ranking/popular 에서 뉴스 랭킹 목록 가져오기 위함.
    req = requests.get("https://news.daum.net/ranking/popular")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_daum_news = []
    list_daum_news_href =[]

    for i in soup.select("#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong"):
        list_daum_news.append(i.find("a").text)
        list_daum_news_href.append(i.find("a")["href"])

    return list_daum_news, list_daum_news_href

# 오늘의 유머
def today():
    req = requests.get("http://www.todayhumor.co.kr/board/list.php?table=bestofbest")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_today = []
    list_today_href = []

    for i in soup.find_all("td", class_="subject"):
        list_today.append(i.text)
        list_today_href.append("http://www.todayhumor.co.kr" + i.find("a")["href"])

    return list_today, list_today_href

# OKKY
def okky():
    req = requests.get("https://okky.kr/articles/tips")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_okky = []
    list_okky_href = []

    for i in soup.select("#list-article > div.panel.panel-default > ul > li > div.list-title-wrapper.clearfix > h5"):
        list_okky.append(i.find("a").text)
        list_okky_href.append("https://okky.kr" + i.find("a")["href"])

    return list_okky, list_okky_href
