from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests

if __name__ == '__main__':
    url = "https://www.youtube.com/feed/trending"
    with requests.post(url) as response:
        soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    # youtube_titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"})
    youtube_titles = soup.select("a.yt-uix-tile-link")
    for youtube_title in youtube_titles:
        print(youtube_title.text)