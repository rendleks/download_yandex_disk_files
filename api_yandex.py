import requests
from urllib.parse import urlencode
import csv
import os
import subprocess


def get_href(public_link):
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

    final_url = base_url + urlencode(dict(public_key=public_link))
    response = requests.get(final_url)
    parse_url = response.json()['href']
    download_url = requests.get(parse_url)
    print("Скачивание успешно!", public_link)


get_href('https://disk.yandex.ru/d/74xEHTD3tabF-w')