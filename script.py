import os
message = input("Enter commit message: ")
os.system("git add .")
os.system("git commit -m \"" + message + "\"")
os.system("git push -u origin master")
