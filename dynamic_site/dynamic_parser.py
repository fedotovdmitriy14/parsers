from bs4 import BeautifulSoup
import requests
import lxml

url = "http://www.edutainme.ru/edindex/"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

r = requests.get(url=url, headers=headers)

print(r.text)

# with open("index.html", "w") as file:
#     file.write(r.text)
#
# # get hotels urls
# r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most", headers=headers)
# soup = BeautifulSoup(r.text, "lxml")