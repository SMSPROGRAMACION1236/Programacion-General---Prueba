## Aqui es donde probaremos las funcionalidades
### Es buena practica crear un archivo con el nombre test_c en donde c es el nombre del archivo a probar como el nombre de este archivo

import pytest
from src.main import suma, es_mayor_que, login
def test_suma():
  assert suma(1, 2) == 3 # Esta es una prueba, evaluamos si el retorno de la funcion suma(1,2) es igual 3 cual si cumple
#! Ejecutamos en la consula pytest, este automaticamente detecta todas las pruebas
""" Si le ponemos -v sera mas expresivo"""


def test_es_mayor_que():
  assert es_mayor_que(5, 2) == True # Esta es una prueba
  
#* Para hacer varias pruebas con muchas datos

@pytest.mark.parametrize(
  #Especificamos que variables utilizaremos
  "value1, value2, expected",
  [#
   #Los datos de entrenamiento
    (1, 2, 3),
    (2, 2, 4),
    (3, 3, 6)
  ]
)
def test_suma_parametros(value1,value2, expected):
  assert suma(value1, value2) == expected
  
  
def test_login_pass():
  login_passes = login("santipro","123")
  assert login_passes
def test_login_fail():
  login_fail = login("santiproxd","1234")
  assert  not login_fail # Esperamos que sea falso