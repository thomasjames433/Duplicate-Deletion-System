

import os
import shutil
import Get_Path
def Duplicates(contents):
    if len(contents)!=0 or len(contents)!=1:
        for i in range(len(contents)):
            m=Get_Path.PATH(contents[i])
            if not os.path.exists(m+"Duplicates"):
                os.mkdir(m+"Duplicates")
            shutil.move(contents[i],m+"Duplicates")



# m=['Other/CS02/IMG-20231211-WA0093.jpg', 'Other/CS02/IMG-20231211-WA0094.jpg']
# Duplicates(m)