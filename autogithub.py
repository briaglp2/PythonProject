import os


info = input("Entrer les informations qui ont été modifier: ")
os.system("git add .")
os.system("git commit -m "+info+" ")
os.system("git push -u PythonProject master")