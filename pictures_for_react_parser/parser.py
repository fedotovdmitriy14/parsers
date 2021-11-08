import asyncio
import concurrent
import time

from bs4 import BeautifulSoup
import requests



t1 = time.perf_counter()

def get_pictures():
    url = "https://github.com/divanov11/proshop_django/tree/master/static/images"
    r = requests.get(url)
    response = r.content

    soup = BeautifulSoup(response, 'lxml')
    pictures = soup.find_all('a', class_="js-navigation-open Link--primary")
    number = 0

    for pic in pictures:
        number += 1
        print(f"Downloading picture {number}")
        url = "https://github.com" + pic.get("href")
        r = requests.get(url).content

        # get_pic_url(number, r)
        soup = BeautifulSoup(r, "lxml")
        img = soup.find("div", class_="text-center p-3").find("img").get("src")
        img_url = "https://raw.githubusercontent.com" + img.replace("?raw=true", "")
        img_url = img_url.replace("/blob/master", "/master")
        img = requests.get(img_url).content
        with open(f"pictures/{number}.jpg", "wb") as f:
            f.write(img)

# def get_pic_url(number, url):
#     soup = BeautifulSoup(url, "lxml")
#     img = soup.find("div", class_="text-center p-3").find("img").get("src")
#     img_url = "https://raw.githubusercontent.com" + img.replace("?raw=true", "")
#     img_url = img_url.replace("/blob/master", "/master")
#     img = requests.get(img_url).content
#     with open(f"pictures/{number}.jpg", "wb") as f:
#         f.write(img)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_pictures())
#     executor.submit(get_pictures())

# get_pictures()

t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')




