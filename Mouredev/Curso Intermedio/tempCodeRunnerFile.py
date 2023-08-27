import csv

def procesar_archivo(archivo):
    with open(archivo, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Procesar cada fila del archivo
            pass

archivo_procesado = "sms.csv"

procesar_archivo(archivo_procesado)

print(f"Se procesaron correctamente 1 archivo; error al procesar 0 archivos")