from flask import Flask, render_template
app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello():
    # https://news.daum.net/ranking/popular 에서 뉴스 랭킹 목록 가져오기 위함.
    req = requests.get("https://news.daum.net/ranking/popular")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_daum = []

    for i in soup.select("#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong"):
        list_daum.append(i.find("a").text)

    return render_template("index.html", daum = list_daum)

@app.route('/about')
def about():
    return "여기는 about입니다."

if __name__ == '__main__':
    app.run()