--*Consultas de Búsqueda:


-- Encuentra todos los usuarios cuyos nombres contienen la letra “o”.


SELECT Nombre as Nombre_con_O FROM Usuarios
WHERE Nombre like "O%";


-- tra los registros de la tabla “Usuarios” ordenados alfabéticamente por nombre.

SELECT * FROM Usuarios
ORDER BY Nombre ASC;


--* Consultas de Actualización:
-- Cambia el nombre del usuario con Id igual a 2 a “Olivia”.

UPDATE  Usuarios
set Nombre = "Olivia"
WHERE id = 2;


-- Actualiza la edad del usuario con Id igual a 1 a 30 años.

UPDATE Usuarios
SET Edad = 30
WHERE id = 1;

--* Consultas de Eliminación:
-- limina el usuario con Id igual a 3.

DELETE 	FROM Usuarios
WHERE id = 3;

--* Consultas de Agregación:
-- alcula la edad promedio de todos los usuarios.

SELECT round(avg(Edad)) as edad_promedio from Usuarios;



-- Encuentra el usuario más joven (con la menor edad).

SELECT min(Edad) as edad_minima FROM Usuarios;


--* Consultas con Filtros:
-- Muestra los nombres de los usuarios mayores de 25 años.

SELECT  Nombre FROM Usuarios

WHERE Edad >30;
-- uestra los nombres de los usuarios cuyas edades están entre 20 y 30 años.

SELECT * FROM Usuarios
WHERE Edad BETWEEN 20 AND 30

