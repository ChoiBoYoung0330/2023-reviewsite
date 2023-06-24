## [reviewsite] 영화/드라마 리뷰점수 분석 사이트

## 프로젝트 소개
평점만 제공되는 기존 시스템을 작품마다 다른 핵심 키워드를 통해 평점을 세분화시켜주는 새로운 시스템으로 서비스를 제공.

## 프로젝트의 필요성
사람들은 보통 보고싶은 영화나 드라마를 보기 전에 다른 사람들은 재밌게 봤는지 무슨 내용인지 궁금해서 리뷰를 찾아보곤 합니다.

유명한 리뷰사이트인 IMDB, Rotten Tomatoes에서는 각각 총 평점/회차별 평점/나라별 평점, 긍정리뷰와 3.5점 이상인 점수의 퍼센트를 제공하고 있습니다. 또한 우리나라의 대표적인 포털사이트 다음에서는 네트즌 평점을, 네이버에서는 감상포인트를 제공하고 있습니다. 네이버에서는 OST/영상미/스토리/연기/연출에 해당하는 감상초인트를 제공하지만 모든 장르의 모든 작품에 똑같이 적용되고 있습니다. 또한 각 항목이 평점에 얼마나 영향을 끼쳤는지 산출방법을 알 수 없습니다.

이러한 정보들을 토대로 대부분의 사람들은 재밌게 봤구나 재미없구나를 알 수 있겠지만 사람마다 평점이 높은 작품이 모두에게 재미있을 수 없듯이 작품을 볼 때 중요하게 생각하는 부분은 사람마다 모두 다릅니다. 하지만 현재 제공하는 정보만으로는 각자의 생각과 니즈를 충족시킬 수 없습니다.

그래서 어떤 작품을 볼까 고민될 때 내가 중요하게 생각하고 보고싶은 작품을 잘 설명할 수 있는 핵심 키워드를 제공하여 유저에게 도움을 줄 수 있고, 작품별 다른 핵심 키워드를 제공함으로써 배경, 배우, 장르 등 작품을 설명할 수 있는, 평점을 세분화한 핵심 키워드를 방사형 그래프를 통해 제공해주는 리뷰사이트를 구현하게 되었습니다.

## 구현 순서
[crawling]-[NLP]-[TF-IDF]-[django]

## crawling - crawling.py
python selenium을 이용해서 사이트 '키노라이츠'에 있는 작품을 crawling.

후에 tf-idf 계산을 위해 리뷰 수가 너무 적지 않은 50개 이상의 리뷰가 존재하는 작품만을 사용.

또한 tf-idf에 사용하는 단어에서 작품명과 극 중 이름을 제외하기 위해 리뷰뿐만 아니라 작품명과 극 중 이름도 crawling하고 추가로 성을 뺀 이름도 저장.

## NLP - lemma.py
konlpy 라이브러리 사용.

stop_words_list에는 title과 배우들의 이름이 저장되고 lemmatized_words에는 stop_words_list에 있는 단어들을 제외한 단어들만이 저장.

## TF-IDF - tf_idf.ipynb
tf-idf를 구하고 단어들의 개수와 평균점수를 내림차순으로 정렬하여 상위 20개의 단어만 작품별로 엑셀 시트에 저장.

## django - projects/, venvs/
### - venvs/

venvs/reviewsite/bin/activate 으로 가상환경을 통해 프로젝트를 진행.

### - projects/reviewsite/pybo/models.py

database는 sqlite를 사용. pybo의 models.py에서 basic_info, detail_info, graph, review_info 테이블을 생성. basic_info의 title key를 참조하는 외래키 title을 모두 가지고 있음.

### - projects/reviewsite/pybo/views.py
웹사이트를 구성하기 위한 정보들을 제공하기 위한 .html에 사용될 정보들을 저장.

### - projects/reviewsite/templates/pybo/
basic_info_list.html은 웹사이트의 메인 화면을 구성하는 파일.

title_detail.html은 메인 화면에 있는 작품 하나를 클릭할 경우 들어가지는 작품의 상세페이지에 해당하는 파일.

방사형 그래프는 title_detail.html에 chart.js로 구현.

### - projects/reviewsite/static/
style.css는 basic_info_list.html, review_style.css는 title_detail.html에 사용.

## 웹사이트 열기

### 가상환경 진입
[소융캡]-[projects]로 먼저 이동한 후에

    source Users/choiboyoung/소융캡/venvs/reviewsite/bin/activate
    cd reviewsite

위의 코드를 실행하여 가상환경에 진입.
### 웹사이트 열기

    python manage.py runserver

위의 코드를 실행하면 "Starting development server at http://~"의 정보가 주어지고 "http://"에 해당하는 장고 서버 실행.

## 향후 계획
1. 단어 정규화를 통한 리뷰 텍스트 분석의 고도화
2. 핵심 키워드 자동 추출 알고리즘 개선
3. 웹페이지의 기능 추가
4. 웹페이지의 리뷰 가독성 개선을 위한 키워드별 버튼식 리뷰제공
