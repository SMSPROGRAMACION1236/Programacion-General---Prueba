--- SELECT all the Titles

SELECT Title FROM IMDB;


-- Filtrar por genero

/* Muestra las peliculas del genero comedy*/

SELECT  (SELECT Title FROM IMDB WHERE  generes.Movie_id = Movie_id ) as Comedy_Titles
FROM genre as generes
WHERE genre = "Comedy";

 
--- Buscar por titulo
/* Encuentra peliclas que contengan la palabra war en su titutlo, puedes usar el operador like para busquedar parciales*/
SELECT Title FROM IMDB
WHERE Title like "%War%";

-- Top peliculas por recaudacion

/*Ordena las películas de mayor a menor recaudación mundial (worldwide_gross).*/

SELECT Worldwide, (SELECT Title FROM IMDB WHERE money.Movie_id = Movie_id) as revenue
FROM earning as money
ORDER by Worldwide DESC;

-- Promedio de presupuestos
/*Calcula el presupuesto promedio de las películas. Puedes usar la función AVG*/
SELECT round(avg(Budget)) as average_budget FROM IMDB;

-- Peliculas mas antigua
/* selecciona las 10 peliculas mas antiguas de la base de datos*/

-- No hay ninguna tabla o campo referente a la fecha


PRAGMA table_info(genre);



