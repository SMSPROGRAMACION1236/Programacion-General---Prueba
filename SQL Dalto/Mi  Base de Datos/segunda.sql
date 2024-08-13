--Crear una Tabla de Productos:
-- Crea una tabla llamada “Productos” con los siguientes campos:
-- Id (clave primaria, autoincremental)
-- Nombre (cadena de texto)
-- Precio (decimal


--*Ejercicio 2
-- Inserta al menos tres registros en la tabla “Productos” con diferentes nombres y precios.

INSERT INTO Productos ("Product_Name", "Precio") VALUES ('fanta', 30);



--* Ejercicio 3 

-- Realiza las siguientes consultas:
-- Muestra todos los registros de la tabla “Productos”.
-- Muestra los nombres de los productos con un precio mayor a $10.

SELECT Product_Name FROM Productos
WHERE Precio >10


--* Ejercicio4

-- Actualizar Datos:
-- Actualiza el precio del producto con Id igual a 2 a $15.


UPDATE "Productos"
SET "Precio" = 15
WHERE "Product_ID" = 6;


SELECT * FROM "Productos"

--* Ejercicio 5:
--Elimina el producto con Id igual a 3.

DELETE FROM "Productos"
WHERE +"Product_ID" = 8;


SELECT * FROM "Productos"
--* Ejercicio 6
-- Muestra los nombres de los productos cuyos precios están entre $5 y $20.


SELECT * FROM "Productos"
WHERE "Precio" BETWEEN 5 AND 20


