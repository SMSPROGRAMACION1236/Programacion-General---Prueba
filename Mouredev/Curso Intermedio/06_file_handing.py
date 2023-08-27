### file_handing  ###

#.txt file

texto = open("Mouredev\Curso Intermedio\sms.txt", "w+") 

texto.write("""Mi nombre es Santiago
Mi apellido es Sanabria
Mi edad es 15 años
Mi Language favorito es PythonAuque me gusta tambien Rust Auqnue me gusta tambien Rust
Auque me gusta tambien Rust""") # Se debe cambiar a modo de escritura con w+
print(texto.read())
print(texto.read(10))
print(texto.readline())  # Regresa el primer miembros
print(texto.readline())# Segundo
print(texto.readline())
print(texto.readlines()) #regresa 3 Y 4 LINEAS

for line in texto.readline():
    print(line)

texto.write("\nAuque me gusta tambien Rust") # Como escribir desde aqui en otro fichero


import os

texto.close()
# # os.remove("Mouredev\Curso Intermedio\sms.txt") # Para eliminar ficheros


# .json file #


import json


json_file = open("Mouredev\Curso Intermedio\sms.json", "w+")  # Para crear archivos
    

json_test = {
    "name":"Santiago",
    "surname":"Sanabria",
    "age":15,
    "language":["Python", "Rust", "Go"],
    "website": "https://google.com" }


json.dump(json_test, json_file, indent=4)  # con dump puedes escribir en un fichero de json y la indentacion seria la sangria
# json.dump(json_test, json_file, indent=4)  # con dump puedes escribir en un fichero de json y la indentacion seria la sangria

json_file.close()

with open("Mouredev\Curso Intermedio\sms.json") as  my_other_file:
    for line in my_other_file.readline():
        print(line)


json_dict = json.load(open("Mouredev\Curso Intermedio\sms.json"))

print(json_dict)

print(json_dict["name"]) # Para acceder a un dato

# .csv file#

import csv
csv_file = open("Mouredev\Curso Intermedio\shms.csv", "w+")  # Para crear archivos

csv_writer= csv.writer(csv_file)


csv_writer.writerow(["name", "surnmae", "age", "language", "website"])
csv_writer.writerow(["Santiago", "Sanabria", "15", "Python", "https://google.com"])
csv_writer.writerow(["M", "G", "15", "Rujby", ""])

with open("Mouredev\Curso Intermedio\shms.csv") as  my_other_file:
    for line in my_other_file.readline():
        print(line)
#.xlsx file
# import xlrd  se debe instalarse el modulo

#.xml file 
import xml

