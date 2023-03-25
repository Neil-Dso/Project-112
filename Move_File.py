import os
import shutil

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Desktop/Neil/Coding/Python/Project_111/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, ext = os.path.splitext(i)
    print(name, '\t', ext)

    if ext == "":
        continue
    if ext in [".txt", ".docx", ".doc", ".pdf", ".png", ".jpg"]:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + i

        if os.path.exists(path2):
            print('Moving', i, 'to', path2)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print('Moving', i, 'to', path2)
            shutil.move(path1, path3)