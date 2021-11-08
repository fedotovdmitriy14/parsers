from lxml import etree
import requests


def get_and_convert_currency():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url=url)

    with open('currency.xml', 'w') as file:
        file.write(r.text)

    with open('currency.xml', 'rb') as f:
        xml = f.read()

    root = etree.fromstring(xml)

    currency_dict = {}
    for element in root.getchildren():
        n = element.getchildren()
        for i, elem in enumerate(n):
            if elem.text == 'Венгерских форинтов' or elem.text == 'Норвежских крон':
                currency_dict[elem.text] = []
                currency_dict[elem.text].append(int((n[i - 1].text)))
                currency_dict[elem.text].append(n[i + 1].text)
                break

    return currency_dict


print(get_and_convert_currency())