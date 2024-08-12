from fastapi import APIRouter # Inportamos


router = APIRouter(prefix="/products", ## Quiere decir que no es necesario mas adelante indicar la url
                   tags=["products"], # Para agrupar en la documentacion
                    responses={404: {"message":"no encontrado"}})  #luego poner el error defaut del api





products_list= ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
  return products_list


 
@router.get("/{id}")
async def products(id:int):
  return products_list[id]

 