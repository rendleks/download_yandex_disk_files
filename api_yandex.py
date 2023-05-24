import requests
from urllib.parse import urlencode
import csv
import os
import zipfile


def get_href(public_link):
    """
    Получение ссылки для скачивания
    """
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    #"https://cloud-api.yandex.net/v1/disk/public/resources?public_key=https://disk.yandex.ru/d/IUnNFlWqv9HRzg"
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
    final_link = os.path.join(destination_folder, filename)
    with open(final_link, 'wb') as ff:
        ff.write(download_url.content)
    
    print("Скачан файл: ", filename)
    
    return final_link


def unzip_files(path_to_zip):
    """
    Распаковывает файлы в папку unzip_files
    """
    cur_path = os.getcwd()
    dest_unzip = 'unzip_files'
    path_to_folder, filename = os.path.split(path_to_zip)
    name, extention = os.path.splitext(filename)

    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(dest_unzip)

    return [
        os.path.join(cur_path, dest_unzip, name, file) 
        for file in os.listdir(os.path.join(dest_unzip, name))
        ]


def main():
    try:
        with open('test_url.csv', 'r', encoding='utf-8', newline="") as read_file:
            reading = csv.reader(read_file)
            for row in reading:
                href = str(*row)
                with open('result_data.csv', 'a', encoding="utf-8", newline="") as csv_write:
                    writer = csv.writer(csv_write, delimiter=",")
                    writer.writerow(
                        [
                        href, 
                        *unzip_files(download_files(get_href(href))),
                    ]
                    )
    except FileNotFoundError:
        print("Файл не найден!")
    
    finally:
        print("Well Done!")


if __name__ == "__main__":
    main()