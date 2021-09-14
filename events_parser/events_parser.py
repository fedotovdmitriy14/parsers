import requests
from bs4 import BeautifulSoup
import lxml
import json




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

link_urls = []

for i in range(0, 96, 24):
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=13 Sep 2021&to_date=&maxprice=500&o={i}&bannertitle=September"

    req = requests.get(url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]
    print(f"collecting info {i}")

    # with open(f"event_list/index_{i}.html", "w") as file:
    #     file.write(html_response)

    with open(f"event_list/index_{i}.html", "r") as file:
        content = file.read()

    soup = BeautifulSoup(content, "lxml")
    cards = soup.find_all("a", class_="card-details-link")

    for card in cards:
        card_href = "https://www.skiddle.com/" + card.get("href")
        link_urls.append(card_href)

count = 0
list_result = []
for url in link_urls:
    count += 1
    print(count)
    print(url)

    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, "lxml")
        fest_info_block = soup.find("div", class_="top-info-cont")

        name = fest_info_block.find("h1").text.strip()
        date = fest_info_block.find("h3").text.strip()
        location_url = "https://www.skiddle.com" + fest_info_block.find("a", class_="tc-white").get("href")


        req = requests.get(url=location_url, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")

        contact_details = soup.find("h2", string="Venue contact details and info").find_next()
        items = [item.text for item in contact_details.find_all("p")]

        contact_details_dict = {}
        for contact_detail in items:
            contact_detail_list = contact_detail.split(":")

            if len(contact_detail_list) == 3:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip() + ":" \
                                                                       + contact_detail_list[2].strip()
            else:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip()

        list_result.append(
            {
                "Fest name": name,
                "Fest date": date,
                "Contacts data": contact_details_dict
            }
        )

    except Exception as ex:
        print(ex)

with open("event_list/list_result.json", "a", encoding="utf-8") as file:
    json.dump(list_result, file, indent=4, ensure_ascii=False)

print(link_urls)



