import os
import random

def renomear_arquivos():

    list_files = os.listdir(r"F:\lab\udacity\alphabet\alphabet\message")
    print(list_files)

    os.chdir(r"F:\lab\udacity\alphabet\alphabet\message")
   
    for file_name in list_files:
        os.rename(file_name, str(random.randint(1,21)) + file_name)
        

renomear_arquivos()
