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
                correct_format_price = n[i + 1].text.replace(',', '.')
                currency_dict[elem.text].append(float(correct_format_price))
                break

    one_crone = currency_dict['Норвежских крон'][1] / currency_dict['Норвежских крон'][0]

    one_forint = currency_dict['Венгерских форинтов'][1] / currency_dict['Венгерских форинтов'][0]

    print(currency_dict)

    return one_crone / one_forint


print(get_and_convert_currency())

