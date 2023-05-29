# download_yandex_disk_files

Программа для скачивания с яндекс диска. На вход подаётся файл csv с ссылками на яндекс диск. На выходе получаем скаченные файлы, а так же файл с путями до этих файлов у вас на компьютере.

![статья написана для Pikabu](/img/pikabu.png)


### Установка и запуск

```
$ git clone https://github.com/rendleks/download_yandex_disk_files.git

$ cd download_yandex_disk_files

$ pip install -r requirements.txt

$ python api_yandex.py path_to_file.csv
```


### Файл с рультатом имеет вид (ссылка, полный путь до файла)

![relult_data.csv](/img/csv-result.jpg)