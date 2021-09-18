import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# # url = "https://rutube.ru/channel/23642865/videos/"
# url2 = "https://rutube.ru/feeds/5channel/"
# options = webdriver.ChromeOptions()
# # options.set_preference("general.useragent.override",
# #                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
#
# driver = webdriver.Chrome(executable_path='C:\\Users\\dmitr\\Desktop\\python-parsers\\chromedriver.exe', options=options)
#
# try:
#     driver.get(url=url2)
#     time.sleep(1)
#
#     with open('rutube.html', 'w', encoding='utf-8') as file:
#         file.write(driver.page_source)
#
#
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()


with open("rutube.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")
divs = soup.find_all("a", class_="pen-h-card__title")

data_dict = {}

for div in divs:
    data_dict[div.get("href")] = div.get("title")

print(data_dict)

with open("channel_data.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, indent=4, ensure_ascii=False)


# def get_data_from_channel():
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
#     }
#
#     url = "https://rutube.ru/channel/23642865/videos/"
#
#     req = requests.get(url, headers=headers)
#     req.encoding = 'utf-8'
#     req = req.text
#
#     print(req)
#     soup = BeautifulSoup(req, "html.parser")
#     all_videos = soup.find_all("a", class_="pen-h-card__image-wrapper")
#     print(all_videos)
#     video_hrefs = []
#     for video in all_videos:
#         print(video)
#         video_hrefs.append(video.get("href"))
#
#     return video_hrefs
#
# print(get_data_from_channel())