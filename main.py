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
    
    try:
        with open(file_links, newline='') as File:  
            reader = csv.reader(File)
            i = 1
            for row in reader:
                public_key = str(*row)
                
                # Получаем загрузочную ссылку
                final_url = base_url + urlencode(dict(public_key=public_key))
                print(final_url)
                response = requests.get(final_url)
                download_url = response.json()['href']
                # Загружаем файл и сохраняем его
                download_response = requests.get(download_url)
                key = public_key.replace("https://disk.yandex.ru/d/", "")
                with open(f"{download_folder}\{key}.zip", 'wb') as f:   # Здесь укажите нужный путь к файлу
                    f.write(download_response.content)

                print(f"Cкачано файлов {i}", public_key)
                i += 1
    except Exception as e:
        print("Внимание! Не указан или не обнаружен файл с ссылками!\n", e)



def extract_zip(zip_in_folder):
    all_zip = os.listdir(f".\\{zip_in_folder}")
    z = os.path.abspath('.\\files_zip')
    
    #z_path = os.path.join(z,all_zip)

    path_7zip = "C:\\7zip\\7za.exe"
    path_working = f"C:\\Users\\internetshop17\\pars\\migliore_yandex\\{zip_in_folder}"
    os.chdir(path_working)
    for num, i in enumerate(all_zip):
        base = os.path.basename(i).split('.')[0]
        ret = subprocess.check_output([path_7zip, "x", f"-o{base}", i])
        print(num, base)


def get_all_files_path(folder_pic, file_name):

    all_folder = os.listdir(f".\\{folder_pic}")
    z = os.path.abspath(f'.\\{folder_pic}')
    path_folders = []

    for file in all_folder:
        if not file.endswith(".zip"):
            path_folders.append(file)

    for folder in path_folders:
        z_path = os.path.join(z, folder)
        os.chdir(z_path)
        for i in os.listdir(): 
            end_folder = os.path.abspath(i)
            with open(f"C:\\Users\\internetshop17\\pars\\migliore_yandex\\{file_name}", 'a', encoding="utf-8", newline="") as f:
                writer = csv.writer(f, delimiter=";")

                if os.path.isdir(end_folder):
                    writer.writerow([folder, end_folder, [os.path.join(os.sep, end_folder, i) for i in os.listdir(end_folder)]])
                else:
                    writer.writerow([folder, end_folder, [os.path.join(os.sep, end_folder, i) for i in os.listdir(z_path)]])
                    

def main():
    links_for_download = "scheme_item.csv" # вставить наименование файла с ссылками
    folder_for_download = "scheme" # папка для сохранения, придумать имя
    name_file_result = "sheme_result.csv" # наименование файла с результатом

    # примечание. Нужно установить 7zip. В данном случаи это папка C:\\7zip\\7za.exe

    download_files(links_for_download, folder_for_download)
    # extract_zip(folder_for_download)
    # get_all_files_path(folder_for_download, name_file_result)


main()