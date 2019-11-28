#pip install beautifulsoup4
#pip install lxml
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > beautifulsoup4 > install
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > lxml > install

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503")
    soup = BeautifulSoup(data,"lxml") #httpResponse -> HTML

    # print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"}) #<td class="title">...</td>
    for cartoon_title in cartoon_titles:                          #cartoon_titles[:2]
        title = cartoon_title.find("a").text                      #<a>text</a>
        link = cartoon_title.find("a").get("href")                #태그의 속성값 가져오기, <a href="">text</a?
        link="https://comic.naver.com" + link
        print(title)
        print(link)
        html+="<a href='{}'>{}</a><br/>".format(link,title)
    html += "</body></html>"
    #print(hmtl)
    outputSoup=BeautifulSoup(html, "lxml")  #내가 생성한 html 문자열을 soup 객체로 만들자
    prettyHtml = str(outputSoup.prettify()) #예쁘게 html코드로 만들자
    with open("연애혁명.html","w",encoding="utf-8") as f: #html파일 만들자
        f.write(prettyHtml)

