### Manejos de Paquetes ###

import numpy  # pip install numpy

print(numpy.version.version)  # Para saber si esta instalado


numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array * 2)

import pandas #pip install pandas

#pip list Para saber lo que tenemos en total tod


#pip uninstall pandas Para desistalar paquetes

#pip show numpy Para saber informacion sobre este paqute

#pip -- version  Para saber la version


import requests # Trabajar con la APIs
#  Aqui hablamos con la APIs


response =  requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response)
print(response.status_code)
print(response.json())  # Los nombres de esos poquemones 

# Arimetria Package 
from mypackage import arimetria  #  debemos de aclarar que sacaremos un modulo de un paquete

print(arimetria.sum_two_values(2, 4))

from myotherpackage import other_arimetria

print(other_arimetria.sum_two_values(2, 4))
print(other_arimetria.sum_two_values(2, 4))
print(other_arimetria.sum_two_values(2, 48))
print(other_arimetria.sum_two_values(2, 46654))
print(other_arimetria.sum_two_values(2, 45666))
print(other_arimetria.sum_two_values(2, 3))
print(other_arimetria.sum_two_values(2, 3))
print(other_arimetria.sum_two_values(2, 4))
print(other_arimetria.sum_two_values(2, 43))