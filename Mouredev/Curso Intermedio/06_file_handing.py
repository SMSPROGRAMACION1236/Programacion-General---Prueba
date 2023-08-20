### file_handing  ###

#.txt file

texto = open("Mouredev\Curso Intermedio\sms.txt", "w+") 

texto.write("""Mi nombre es Santiago
Mi apellido es Sanabria
Mi edad es 15 años
Mi Language favorito es PythonAuque me gusta tambien Rust Auqnue me gusta tambien Rust
Auque me gusta tambien Rust""") # Se debe cambiar a modo de escritura con w+
# print(texto.read())
# print(texto.read(10))
print(texto.readline())  # Regresa el primer miembros
print(texto.readline())# Segundo
print(texto.readline())
print(texto.readlines()) #regresa 3 Y 4 LINEAS

for line in texto.readline():
    print(line)

texto.write("\nAuque me gusta tambien Rust") # Como escribir desde aqui en otro fichero


import os

texto.close()
os.remove("Mouredev\Curso Intermedio\sms.txt") # Para eliminar ficheros

