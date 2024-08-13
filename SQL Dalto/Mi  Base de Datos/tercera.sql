--* Ejercicios 1
-- Encuentra todos los usuarios cuyos nombres comienzan con la letra “A”.
-- Muestra los registros de la tabla “Usuarios” ordenados alfabéticamente por nombre.
SELECT Nombre FROM Usuarios
WHERE Nombre like "A%";

--* Ejercicio 2
-- Consultas de Actualización:
-- ambia el nombre del usuario con Id igual a 2 a “Ana”.
-- aliza la edad del usuario con Id igual a 1 a 28 años.

UPDATE Usuarios
SET Nombre = "Ana"
WHERE id	= 2;

UPDATE Usuarios
SET Edad = 28
WHERE id = 1;




--* Ejercicio 3
-- Elimina el usuario con Id igual a 3.


DELETE FROM Usuarios

WHERE id = 3;

--* Ejercicio 4
-- Calcula la edad promedio de todos los usuarios.

SELECT round(avg(Edad))as promedio FROM Usuarios;
-- Encuentra el usuario más joven (con la menor edad).

SELECT min(Edad) as edad_minima FROM Usuarios;


--* Ejercicio 5

-- Muestra los nombres de los usuarios mayores de 25 años.
SELECT * FROM Usuarios
WHERE Edad > 25;
-- uestra los nombres de los usuarios cuyas edades están entre 20 y 30 años.

SELECT * FROM Usuarios
WHERE Edad BETWEEN 20 and	30

