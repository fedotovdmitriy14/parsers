import requests
from bs4 import BeautifulSoup
import json

def parse():
    res = requests.get("https://auto.ru/moskva/cars/mitsubishi/outlander/21397304/used/?page=1", "html.parser")
    res.encoding = "utf-8"
    res = res.text

    soup = BeautifulSoup(res, "html.parser")

    items = soup.find_all("div", class_="ListingItem__column ListingItem__column_left")

    car_dict = {}

    for item in items:
        href = item.find("a").get("href")
        description = item.find("div", class_="ListingItemTechSummaryDesktop__column").get_text()
        car_dict[href] = description

    print(car_dict)



parse()
