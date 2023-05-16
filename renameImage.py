import os
from PIL import Image


current_folder = os.getcwd()
#folder_rename = 'aquatek_resize'
folder_source = 'aquatek_data_files'
folder_dest = 'aquatek_resize'

files_in_folder = os.path.join(current_folder, folder_source)
files_in_dest = os.path.join(current_folder, folder_dest)

for folders in os.listdir(files_in_folder):
    rename_folder_files = os.path.join(files_in_folder, folders)
    for files in os.listdir(rename_folder_files):
        file_name, extention = os.path.splitext(files)
        name_source = os.path.join(rename_folder_files, files)
        if extention in ".png":
            file_path = os.path.join(rename_folder_files, files)
            #print(file_path)
            rename_file = file_name.replace("%", "-") # меняем пробелы в названии на "-"
            try:
                img = Image.open(file_path)
                background = Image.new('RGBA', img.size, (255, 255, 255))
                alpha_composite = Image.alpha_composite(background, img)
                jpg_image = alpha_composite.convert('RGB')
                #img = img.convert('RGB')
                new_file_path = os.path.join(current_folder, folder_dest, folders, rename_file + ".jpg")
                jpg_image.save(new_file_path)
                print(new_file_path)
            except Exception as e:
                print(folders, e)

            
            # name_distination = os.path.join(rename_folder_files, rename_file + extention)
            # print(name_source, name_distination)
            # os.rename(name_source, name_distination)


print("Готово!")