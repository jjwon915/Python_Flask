# Python_Flask

인프런의 실시간 트렌드 홈페이지 개발 강의를 참고해 진행했다. 첫번째 프로젝트는 다음, 오늘의 유머, 클리앙이라는 사이트의 실시간 검색어, 인기글들의 제목과 그 글의 링크를 크롤링 해오는 프로젝트이다. 하지만 다음의 실시간 검색어가 사라져 다음 뉴스 랭킹의 뉴스 기사들을 크롤링 했고 나름 응용을 해보기 위해 클리앙이라는 사이트 대신 OKKY사이트의 글들을 크롤링해보았다. 


<crawling.py>
- 크롤링 라이브러리를 import한다.

- 크롤링 하기 위한 사이트를 request.get에 써준다. 아래 예시에서는 다음 뉴스 랭킹 사이트를 이용했다.

- list_daum_news는 크롤링한 제목들을 담는 리스트, list_daum_news_href는 크롤링한 링크를 담는 리스트이다.

- a 태그 전까지 반복되는 태그의 구문을 찾아 copy selector를 한 뒤 작성해준다.( a태그 안의 글을 받아오기 위해 strong 태그까지 copy selector를 했고 copy selector한 것을 붙여넣기 하면 이런 식으로 나오게 된다. #mArticle > div.rank_news > ul.list_news2 > li:nth-child(1) > div.cont_thumb > strong 여기서 li:nth-child(1)을 li 로 바꿔주면 된다.)

- a 태그 안의 텍스트를 list_daum_news에 append하고 href를 찾아 링크를 list_daum_news_href에 append해준다.

<app.py>
- Flask를 사용하기 위해 import 해준다.

- crawling.daum_news()함수를 통해 받아온 값을 index.html로 넘겨준다.

- daum_len은 받아온 제목들의 개수를 나타낸다.

<index.html>
- daum_len 만큼 for문이 실행되도록 구현한다.

-  크롤링한 내용이 하이퍼링크와 함께 화면에 나오게 되며 해당 페이지로 이동할 수 있다.
