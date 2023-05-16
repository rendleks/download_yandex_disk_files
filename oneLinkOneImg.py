import requests
from urllib.parse import urlencode
import csv
import os
import subprocess

def download_files(file_links, download_folder):
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    # public_key = 'https://disk.yandex.ru/d/74xEHTD3tabF-w'  # Сюда вписываете вашу ссылку

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    
    data = []
    with open(file_links, newline='') as File:  
        reader = csv.reader(File)
        for file in reader:
            data.append(*[i.split() for i in file])
        
    for num, row in enumerate(data, 1):

        create_folder = row[0] # имя папки для сохранения фото
        path_to_folder = f"{download_folder}\\{create_folder}" # путь до папки с файлами

        if not os.path.exists(path_to_folder):
            os.makedirs(path_to_folder)

        files_in_folder = []
        for num_1, public_key in enumerate(row[1:], 1):

            # Получаем загрузочную ссылку
            final_url = base_url + urlencode(dict(public_key=public_key))
            try:
                response = requests.get(final_url)
                download_url = response.json()['href']
                start_filename = download_url.find('filename=')
                end_filename = download_url[start_filename:].find('&')
                end_name = start_filename + end_filename
                key = download_url[start_filename:end_name][9:]
                files_in_folder.append(key)
                # Загружаем файл и сохраняем его
                download_response = requests.get(download_url)
                #key = public_key.replace("https://disk.yandex.ru/d/", "")
                with open(f"{path_to_folder}\\{key}", 'wb') as f:   # Здесь укажите нужный путь к файлу
                    f.write(download_response.content)

                print(f"Cкачано файлов {num_1}", create_folder, key)
                                
            except Exception as e:
                print("Внимание! Не указан или не обнаружен файл с ссылками!\n", e)

        with open('result_aquatek.csv', 'a', encoding="utf-8", newline="") as csv_write:
                writer = csv.writer(csv_write)
                writer.writerow([
                    create_folder + "\\" + filename for filename in files_in_folder
                ])
            
        print("Готово! Ссылок.", num, "из 39!")
            

download_files('aquatek.csv', 'aquatek_data_files')

print("Всё прошло успешно!")