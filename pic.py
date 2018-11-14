import os

my_files = os.listdir("/home/allen/request_flask_project")
#print(my_files)

listFiles = []
for files in my_files:
    if ".jpg" in files:
        print(files)
        listFiles.append(files[:-4])

listFiles.sort()
fo = open("jpg.txt", "w")
for fileName in listFiles:
    fo.write(fileName + "\n")
    #print(fileName)
fo.close()
