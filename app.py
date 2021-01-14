from flask import Flask, render_template
app = Flask(__name__)

import crawling

@app.route('/')
def hello():

    list_daum_news, list_daum_news_href = crawling.daum_news()
    list_today, list_today_href = crawling.today()
    list_okky, list_okky_href = crawling.okky()

    return render_template("index.html",
                           daum_news = list_daum_news,
                           today = list_today,
                           okky = list_okky,
                           daum_href = list_daum_news_href,
                           daum_len = len(list_daum_news),
                           today_href = list_today_href,
                           today_len = len(list_today),
                           okky_len = len(list_okky),
                           okky_href = list_okky_href)

@app.route('/about')
def about():
    return "여기는 about입니다."

if __name__ == '__main__':
    app.run()