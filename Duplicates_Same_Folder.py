#has a problem
import os
import shutil

    
def Copy_to_duplicate(string):

    contentsjpg=[]
    if os.path.exists(string):
        contents=os.listdir(string)

        # Takes contents that end with JPG/jpg/mp4
        for i in range(len(contents)):
            if(contents[i][len(contents[i])-3:len(contents[i])]=="JPG" or contents[i][len(contents[i])-3:len(contents[i])]=="jpg"):
                contentsjpg.append(contents[i][0:len(contents[i])-4])           

    # Checks if there is a copy of a file in the same folder and moves it to the folder named "Duplicates"
    copycontents=[]
    for i in range(len(contentsjpg)):
        for j in range(len(contentsjpg)):
            if contentsjpg[i]== contentsjpg[j]+" - Copy" or contentsjpg[i]== contentsjpg[j]+" - Copy (2)" or contentsjpg[i]== contentsjpg[j]+" - Copy (3)" or contentsjpg[i]== contentsjpg[j]+" - Copy (4)":
                if not os.path.exists(string+"/Duplicates"):
                    os.mkdir(string+"/Duplicates")
                shutil.move(string+"/"+f"{contentsjpg[i]}.JPG",string+"/Duplicates")   
    # shutil.rmtree("Ammachi Funeral/Annamma Eattathodu - edited/Duplicates")


# Copy_to_duplicate(input())