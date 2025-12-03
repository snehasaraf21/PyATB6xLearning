import os

print(os.name)#nt-->for windows and poxis for mac
print(os.getcwd())#shows the current working directory
#print(os.mkdir("AI"))#directory with name AI will be created
print(os.listdir())#list all the files in the directory
#print(os.mkdir("AI.txt"))
#print(os.remove("AI.txt"))#removes the file
#print(os.rename("AI","testdata"))
print(os.rename("testdata","Testdata"))#renames the file
print(os.environ.get("PATH"))

