import requests
import img2pdf


def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    img_list = []
    for i in range(1, 49):
        url = f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"images/{i}.jpg", "wb") as file:
            file.write(response)
            img_list.append(f"images/{i}.jpg")
            print(f"Downloaded {i} of 48")

    print("#" * 20)
    print(img_list)

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("Done!")







if __name__ == '__main__':
    get_data()