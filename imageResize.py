import os
from PIL import Image

current_dir = os.getcwd()
#main_folder = 'aquatek_data_files'
main_folder = 'aquatek_resize'
save_to_folder = 'aquatek_resize_ver2'

for folder in os.listdir(main_folder):
    folder_path = os.path.join(current_dir, main_folder, folder)
    # print(folder_path)
    for file in os.listdir(folder_path):

        new_folder_path = os.path.join(current_dir, save_to_folder, folder)
        file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(new_folder_path, file)

        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        file_extension = file.split('.')[-1]
        #print(file, file_extension)

        file_name, file_extension1 = os.path.splitext(file)

        if file_extension != 'pdf':
            print(file)
            #Открываем изображение
            img = Image.open(file_path)
            # Вычисляем новый размер изображения с сохранением пропорций
            width, height = img.size
            if width > height:
                new_width = 1000
                new_height = int(height * (new_width / width))
            else:
                new_height = 1000
                new_width = int(width * (new_height / height))
            # Изменяем размер изображения
            img = img.resize((new_width, new_height))
            # Сохраняем изображение в формате jpeg
            new_file_path_jpg = os.path.join(new_folder_path, file_name, ".jpg")
            if not img.mode == 'RGB':
                img = img.convert('RGB')
            img.save(new_file_path_jpg, 'JPEG')

        else:
            
            os.rename(file_path, new_file_path)
    print("Папка обработана: ", folder)

print("Готово!")
            
                   
        

