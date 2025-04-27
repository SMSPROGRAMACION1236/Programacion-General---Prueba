from django.apps import AppConfig
"""Explicacion: Configuracion de esta aplicacion"""

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
