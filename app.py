from flask import Flask, render_template
app = Flask(__name__)

import crawling

@app.route('/')
def hello():

    list_daum = crawling.daum_news()
    list_today = crawling.today()
    list_okky = crawling.okky()


    return render_template("index.html",
                           daum_news = list_daum,
                           today = list_today,
                           okky = list_okky)

@app.route('/about')
def about():
    return "여기는 about입니다."

if __name__ == '__main__':
    app.run()