import os
import shutil
def Delete_empty_folder(string):

    #Deletes empty folders in a folder
    contents=os.listdir(string)  

    # contentfolders=[]
    for i in range(len(contents)):
        if os.path.isdir(contents[i]):
            if len(os.listdir(string+"/"+f"{contents[i]}"))==0:
                os.rmdir(string+"/"+f"{contents[i]}")
                
# Delete_empty_folder(input())

