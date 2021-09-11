import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://auto.ru/cars/mitsubishi/all/'



def get_html(url, params=None):
    r = requests.get(url, params=params)
    r.encoding = 'utf-8'
    return r



# def get_pages_count(html):
#     soup = BeautifulSoup(html, "html.parser")
#     pagination = soup.find_all('span', class_="Button__content").find_all('span', class_="Button__text")
#     if pagination:
#         return int(pagination[-1].get_text())
#     else:
#         return 1
#     print(pagination)



def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='Link ListingItemTitle__link')

    cars = []
    for item in items:
        cars.append({
            'name': item.get_text()
        })
        try:
            with open("car_data/cars.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        "name:",
                        item.get_text()
                    )
                )
                # file.write(item.get_text())

        except Exception:
            with open("car_data/cars.csv", "w", encoding="utf-8") as file:
                # file.write(item.get_text())
                writer = csv.writer(file)
                writer.writerow(
                    (
                        "name:",
                        item.get_text()
                    )
                )



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        # pages_count = get_pages_count(html.text)
    else:
        print('error')

if __name__ == "__main__":
    parse()
