import os
print(os.getcwd())
x = "C:\\Users\\USER\\AppData\\Local\\Programs"
os.chdir(x)
print(os.getcwd())
print(os.listdir())
os.mkdir("new folder")
print(os.listdir())
