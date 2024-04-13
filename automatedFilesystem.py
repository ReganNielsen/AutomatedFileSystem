# Imported python functions
import os
import shutil

# Select file by using file path in order to automate file manager
path = input("Enter path: ")
files = os.listdir(path)

# For loop - 1. Create file using file extention (e.g. .jpeg) but remove "." by spliting
for file in files:
    filename,extension = os.path.splitext(file)
    #Removing "." from extension to create specific folder
    extension = extension[1:]
    
    # If folder excists then just move file into excisting folder 
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    #Otherwise create folder and move file into newly created folder
    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
