# encargado de gestionar la conexion a mongo tv
from pymongo import MongoClient

#Local Database
# db_client  = MongoClient().local# Si no le ponemos nada para que este en local

#DataBase remote
db_client  = MongoClient("mongodb+srv://sms:sms@cluster0.meyzndz.mongodb.net/?retryWrites=true&w=majority").sms