import requests
from bs4 import BeautifulSoup
import csv
import json

URL = 'https://auto.ru/cars/mitsubishi/all/'
url_pages = "https://auto.ru/moskva/cars/mitsubishi/all/?page=1"



def parse_pages():
    cnt = 1


    while True:
        cars_dict = {}
        res = requests.get(f"https://auto.ru/moskva/cars/mitsubishi/outlander/21397304/used/?page={cnt}", "html.parser")
        res.encoding = "utf-8"
        html = res.text

        soup = BeautifulSoup(html, "html.parser")

        items = soup.find_all('a', class_='Link ListingItemTitle__link')

        if len(items) != 0:
            for item in items:
                car_name = item.get_text()
                car_href = item.get("href")
                cars_dict[car_href] = car_name

            with open(f"car_pages/{cnt}.json", "w") as file:
                json.dump(cars_dict, file, indent=4, ensure_ascii=False)
        else:
            break

        cnt += 1

    print(cars_dict)



parse_pages()


