## Es una funcion que puede ejecutarse en segundo plano, mientras se realiza otra funcion
### await sirve para pausar una funcion y esperar que se realize comandos especificos
import asyncio

async def tarea_1():
  print("Tarea 1: Iniciada")
  await asyncio.sleep(1)  # Simula una tarea que tarda 1segundos
  print("Tarea 1: Finalizada")
  
async def tarea_2():
  print("Tarea 2: Iniciada")
  await asyncio.sleep(2)  # Simula una tarea que tarda 2 segundos
  print("Tarea 2: Finalizada")
async def tareas_en_paralelo():
  # Creamos dos tareas de las funciones tarea_1  y tarea_2
  tarea1 = asyncio.create_task(tarea_1())
  tarea2 = asyncio.create_task(tarea_2())
  # Ejecutar ambas tareas
  await asyncio.gather(tarea1, tarea2)
# Ejecutar la funcion tareas en paralelos
asyncio.run(tareas_en_paralelo())