import requests
from urllib.parse import urlencode
import csv
import os
import subprocess


def get_href(public_link):

    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    final_url = base_url + urlencode(dict(public_key=public_link))
    response = requests.get(final_url)
    parse_href = response.json()['href']
    return parse_href


def download_files(url):
    
    currient_folder = os.getcwd()
    destination_folder = os.path.join(currient_folder, "download_files")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    start_filename = url.find('filename=')
    end_filename = url[start_filename:].find('&')
    end_name = start_filename + end_filename
    filename = url[start_filename:end_name][9:]
    download_url = requests.get(url)
    with open(os.path.join(destination_folder, filename), 'wb') as ff:
        ff.write(download_url.content)
    
    print("Скачан файл: ", filename)


def main():
    #example_link = "https://disk.yandex.ru/d/74xEHTD3tabF-w"
    #download_files(get_href(example_link))
    try:
        with open('list_urls.csv', 'r', encoding='utf-8', newline="") as read_file:
            reading = csv.reader(read_file)
            for row in reading:
                href = str(*row)
    except FileNotFoundError:
        print("Файл не найден!")


if __name__ == "__main__":
    main()