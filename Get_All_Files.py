
import os
import shutil
import Duplicates_Same_Folder

allfiles=[]
def Store_Files(string):
    Duplicates_Same_Folder.Copy_to_duplicate(string)
    contents=os.listdir(string)
    for i in range(len(contents)):
        if not os.path.isdir(string+"/"+f"{contents[i]}"):
            allfiles.append(string+"/"+f"{contents[i]}")
        else:
            # print(contents[i])
            Store_Files(string+"/"+f"{contents[i]}")
    return allfiles

# string=input()
# m=Store_Files(string)
# print(m)
# print(len(m))