import requests
from bs4 import BeautifulSoup


class YoutubeScraper:
    def __init__(self, url):
        self.url = url

    def scrape_video_count(self):
        content = requests.get(self.url)
        soup = BeautifulSoup(content.text, "html.parser")
        view_count = soup.find("div", {"class": "watch-view-count"}).text
        return view_count


url = "https://www.youtube.com/watch?v=VpTKbfZhyj0"
x = YoutubeScraper(url)
x.scrape_video_count()