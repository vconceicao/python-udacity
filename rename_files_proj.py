import os

def renomear_arquivos():

    list_files = os.listdir(r"F:\lab\udacity\alphabet\alphabet\message")
    print(list_files)

    os.chdir(r"F:\lab\udacity\alphabet\alphabet\message")
   
    for file_name in list_files:
        os.rename(file_name, file_name.translate(None, "0123456789") )
        

renomear_arquivos()
