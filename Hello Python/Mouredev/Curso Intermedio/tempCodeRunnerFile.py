
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