
#!Se observa que es muy lento
import time as tm
# def funcion_lenta(n:int) ->int:
#   print(f"Calculando; {n}")
#   tm.sleep(5)
#   print(f"Finalizando: {n}")
#   return n*2

# def main():
#   for i in range(10):
#     funcion_lenta(i)
# if __name__=="__main__":
#   main()
  
#* Concurrencia
import concurrent.futures as cf

def funcion_lenta(n:int) ->str:
  print(f"Calculando; {n}")
  tm.sleep(5)
  return f"El resultado es: {n*2}"

def main():
  entradas = [i for i in range(1000)]
  n_workers = 10000 # Número de hilos a usar, se puede cambiar a 2 o 4 para ver el rendimiento
  with cf.ThreadPoolExecutor(max_workers=n_workers) as executor: # max_workers=3 es el número de hilos, ThreadPoolExecutor es para hilos, ProcessPoolExecutor es para procesos
    #* Se puede usar el método map para obtener los resultados de forma ordenada
    resultados = [executor.submit(funcion_lenta, entrada) for entrada in entradas] # Se usa submit para enviar la función y sus argumentos a los hilos, se puede usar map para obtener los resultados de forma ordenada
    for resultado in cf.as_completed(resultados): # as_completed devuelve un iterador que se completa cuando todos los resultados están listos
      print(resultado.result()) # Se obtiene el resultado de cada hilo, se puede usar map para obtener los resultados de forma ordenada      

if __name__=="__main__":
  main()
  k