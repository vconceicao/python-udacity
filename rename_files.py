import os

def rename_files():

    list_files = os.listdir(r"F:\lab\udacity\prank")
    print(list_files)

    for file_name in list_files:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()
