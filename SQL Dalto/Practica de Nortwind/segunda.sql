--¿Cuántos empleados nacieron después del 1 de junio de 1965? Crea un informe que diga 
--“El empleado Nació el N”, donde “N” representa el nombre completo y la fecha de nacimiento.

SELECT FirstName || ' ' || LastName AS 'Nombre Completo', BirthDate AS 'Nació el'
FROM Employees
WHERE BirthDate > "1965-06-01";


--Repite el informe anterior, pero solo para los empleados con los ID 8, 7, 3 y 10.

SELECT FirstName || ' ' || LastName AS 'Nombre Completo', BirthDate AS 'Nació el'
FROM Employees 
WHERE BirthDate > "1965-06-01" AND EmployeeID  in (8, 7, 3, 1);

--¿Cuáles son los países que tienen más de 5 clientes? 
--Ordénalos alfabéticamente por nombre de país.

SELECT Country, COUNT(*) AS CantidadClientes
FROM Customers
GROUP BY Country;