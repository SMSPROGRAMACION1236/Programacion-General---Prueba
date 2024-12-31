--# Seleccionar todos los datos de una tabla, en este caso de Customers

SELECT * FROM "Customers";

--# Selecciona columnas especificas, para seleccionar solo el nombre y la ciudad de los clientes

SELECT "CustomerName", "City" FROM "Customers";

--# Contar filas, contar el numero de clientes
SELECT count("CustomerName") as "numero_clientes" from "Customers";

--# Filtrar Datos: Encontrar clientes 
SELECT "CustomerName" FROM "Customers"
WHERE "City" = 'London';


--# Cuales son los 5 productos mas caros?

SELECT "ProductName" FROM "Products"
WHERE "ProductName" is not NULL
ORDER by "Price" ASC
limit 5;


--# Cuantos pedidos se realizaron en el año 1997
SELECT count(OrderDate) as pedidos_en_1997 FROM "Orders"
WHERE "OrderDate"  BETWEEN '1997-01-01' AND '1997-12-31';


--# Cual es el cliente que ha hecho mas pedidos

SELECT CustomerID, COUNT(*) AS TotalOrders,(SELECT CustomerName from "Customers")
FROM Orders
GROUP BY CustomerID
ORDER BY TotalOrders DESC
LIMIT 1;