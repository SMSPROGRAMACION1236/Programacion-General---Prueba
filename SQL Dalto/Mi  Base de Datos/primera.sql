SELECT * FROM Usuarios;
-- To insert data into the databse
-- INSERT INTO Usuarios(Nombre, Edad)
-- VALUES ("Peter",42),
-- 	   ("Alex", 32),
-- 	   ("Mary", 53);


/*Consultas SELECT:
Realiza las siguientes consultas: */


-- Muestra todos los registros de la tabla “Usuarios”.


SELECT * FROM Usuarios;
-- Muestra los nombres de los usuarios mayores de 25 años.
SELECT Nombre FROM Usuarios
WHERE Edad > 25;

-- Muestra el nombre del usuario más joven.
SELECT Nombre FROM Usuarios
ORDER By Edad ASC
LIMIT 1;

/* Actualizar Datos */

-- Actualiza la edad del usuario con Id igual a 2 a 30 años.

UPDATE Usuarios
SET Edad = 30
WHERE id = 2;
/*Eliminar Registros*/
-- Elimina el usuario con Id igual a 3.
DELETE FROM Usuarios
WHERE id = 3;

/*Consultas con WHERE*/
-- Muestra los nombres de los usuarios cuyas edades están entre 20 y 30 años

SELECT * FROM Usuarios
where Edad BETWEEN 20 AND 30;
/* Ordenar Resultados*/
-- Muestra los registros de la tabla “Usuarios” ordenados por nombre de forma ascendente.

SELECT * FROM Usuarios
ORDER by Nombre ASC