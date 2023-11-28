import requests as rq
from bs4 import BeautifulSoup
import json


def main():
    url = input("Введите ссылку: ")
    if ("https" or "http") in url:
        data = rq.get(url)
    else:
        data = rq.get("https://" + url)
    soup = BeautifulSoup(data.text, "html.parser")
    links = {}
    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.text
        links[href] = text

    with open('links.json', 'w') as file:
        json.dump(links, file, indent=4, ensure_ascii=False)

    print('Ссылки успешно сохранены в файл links.json')


if __name__ == '__main__':
    main()
