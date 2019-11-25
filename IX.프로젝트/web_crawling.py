#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__=='__main__':
    #네이버웹툰> 연애형멱 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu")
    soup = BeautifulSoup(data, "lxml")          #httpResponse -> HTML
    # print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})    #<td class="title">...</td>
    for cartoon_title in cartoon_titles:                               #cartoon_titles[:2]
        title = cartoon_title.find("a").text                           #텍스트 가져오기.<a>text</a>
        link = cartoon_title.find("a").get("href")                    #태그의 속성값 가져오기, <a href="">text</a>
        link = "https://naver.com" + link
        # print(title)
        # print(link)
        html +="<a href='{}'>{}</a><br />".format(link, title)            #<a href='link'>title</a>
    html += "</body></html>"
    # print(html)
    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("연애혁명.html","w", encoding="utf-8") as f:
        f.write(prettyHtml)