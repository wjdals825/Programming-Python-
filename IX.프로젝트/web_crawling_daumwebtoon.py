#pip install beautifulsoup4
#pip install lxml
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > beautifulsoup4 > install
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > lxml > install

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read())
    # print(j["data"]["webtoon"]["webtoonEpisodes"][3]["title"])
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        # print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        # print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+ str(url)
        # print(url)
        html += "<a href='{}'><img src='{}'/>{}</a>".format(url,thumbnail,title)
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")  # 내가 생성한 html 문자열을 soup 객체로 만들자
    prettyHtml = str(outputSoup.prettify())  # 예쁘게 html코드로 만들자
    with open("취향저격 그녀.html", "w", encoding="utf-8") as f:  # html파일 만들자
        f.write(prettyHtml)