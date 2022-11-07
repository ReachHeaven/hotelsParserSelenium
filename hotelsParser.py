import json
import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "accept": "text/html, */*; q=0.01",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/107.0.0.0 "
                      "Safari /537.36 "
    }

    request = requests.get(url, headers=headers)

    with open("data/index.html", "w") as f:
        f.write(request.text)

    link = "https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most"
    req = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")
        print(hotel_url)


def get_data_with_selenium(url):
    # options = webdriver.ChromeOptions()
    #
    # try:
    #     driver = webdriver.Chrome(
    #         executable_path="/home/karim/repos/dataScrapping/hotelsParser/chromedriver",
    #         options=options
    #     )
    #     driver.get(url=url)
    #     time.sleep(5)
    #
    #     with open("data/index_selenium.html", "w") as f:
    #         f.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()

    with open("data/index_selenium.html") as f:
        src = f.read()

    soup = BeautifulSoup(src, "lxml")

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")
    hotels_dict = {}
    count = 0
    for hotel_url in hotels_cards:
        hotel_url = "https://tury.ru" + hotel_url.find("a").get("href")
        hotels_dict[count]=hotel_url
        count+=1
    with open("hotel_links.json", "a") as f:
        json.dump(hotels_dict, f, indent=4)


def main():
    # get_data("https://tury.ru/hotel/most_luxe.php")
    get_data_with_selenium("https://tury.ru/hotel/most_luxe.php")


if __name__ == '__main__':
    main()
