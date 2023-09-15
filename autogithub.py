import os


os.system("git add .")
info = input("Entrer les informations qui ont été modifier: ")
os.system("git commit -m newsave ")
os.system("git push -u PythonProject master")