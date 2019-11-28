#pip install beautifulsoup4
#pip install lxml
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > beautifulsoup4 > install
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > lxml > install

from urllib.request import urlopen
import json

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read())
    print(j["data"]["webtoon"]["webtoonEpisodes"][3]["title"])
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+ str(url)
        print(url)