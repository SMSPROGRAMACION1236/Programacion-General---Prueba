--* Ejercicio 1: Cuantas peliculas hay en la base de datos

SELECT count(title) as numero_de_peliculas from "IMDB";
--*  EJERCICIO 2: ¿Cuáles son los títulos de las 10 películas mejor calificadas según el rating?
SELECT "Title", "Rating" FROM "IMDB"
ORDER BY "Rating" DESC
LIMIT 10;

--* Ejercicio 3 Cual es la pelicula con mayor recaudacion Mundial
SELECT "Title", "Worldwide" FROM "IMDB" as im, "Earning" as er
WHERE im."Movie_id" = er."Movie_id"
ORDER BY "Worldwide" DESC
limit 1

--* EJERCICIO 4:  ¿Qué géneros de películas están presentes en la base de datos?
SELECT genre FROM genre;

-- * EJERCICIO 5: ¿Cuántas películas tienen un presupuesto mayor a 100 millones de dólares?
select COUNT(title) FROM "IMDB"
where "Budget" > 100000000;

-- * EJERCICIO 6: ¿Cuáles son las películas de ciencia ficción con una duración superior a 2 horas?
-- SELECT title, runtime FROM "IMDB" as im, "genre" as gen
-- WHERE im."Movie_id" = gen."Movie_id" 
-- WHERE "Runtime" > 120
SELECT title, runtime  as cantidad FROM "IMDB" as im
INNER JOIN genre as gen ON im."Movie_id" = gen."Movie_id"
WHERE CAST(SUBSTR(RunTime, 1, INSTR(RunTime, ' ') - 1) AS INTEGER) > 120;
-- * EJERCICIO 7: ¿Qué porcentaje de votos totales provienen de usuarios menores de 18 años?
--! No se cual columna es la que tiene los votos de los menores de 18 años

--* EJERCICIO 8:  ¿Cuál es el género de película más común?
SELECT  count(genre) ,genre as genero_mas_popular FROM genre
WHERE genre IS NOT NULL
GROUP BY genre
ORDER BY count(genre) DESC 
limit 1;

--* EJERCICIO 9:  ¿Cuál es el promedio de calificación de las películas por género?
-- Sabiendo que no se cual de todos es de las calificaciones por que parece que hay varios, tomare solo uno a eleccion en este caso VotesM


SELECT genre, round(avg("VotesM"),2)  as "calificacion_promedio" FROM genre as gen
INNER JOIN "IMDB" as im ON  gen."Movie_id" = im."Movie_id"
GROUP BY genre;

--* EJERCICIO 10:  ¿Cuáles son las 5 películas con mayor recaudación doméstica y sus respectivos géneros?

SELECT title , Domestic, genre FROM "IMDB" as im 
INNER JOIN earning as ear, genre as ge ON ear."Movie_id" = im."Movie_id" and im."Movie_id" = ge."Movie_id"
ORDER BY "Domestic" DESC
LIMIT 5;

-- * EJERCICIO 11: ¿Cuál es el promedio de presupuesto de las películas de acción?
--! No funciona, pero en SQl Browser si
SELECT avg(Budget) as promedio_acccion, genre FROM "IMDB" as im
INNER JOIN genre as ge on im."Movie_id" = ge."Movie_id"

WHERE genre = "Action";

-- * EJERCICIO 12: ¿Cuál es la película con la mayor diferencia entre la recaudación doméstica y mundial?

SELECT title,  "Worldwide" - "Domestic" as  diferencia from "earning" as ear
INNER JOIN "IMDB" as im on ear."Movie_id" = im."Movie_id"
ORDER BY diferencia DESC
limit 1 ;


-- * ¿Cuál es la película con la mayor diferencia entre los votos de hombres y mujeres?

SELECT title, ("CVotesMale" - "CVotesFemale") as diferencia FROM "IMDB"
ORDER BY diferencia DESC
LIMIT 1;

-- * ¿Qué rango de edad (18-29, 30-44, 45+) tiene la mayor participación en las votaciones
SELECT  max(max_votes) as "Max_Vote" from (
SELECT sum("CVotes1829") as "max_votes"  FROM "IMDB"
UNION ALL 
SELECT sum("CVotes3044") as "max_votes"  FROM "IMDB"
UNION ALL  
SELECT sum("CVotes45A") as "max_votes" from "IMDB");

-- * ¿Cuáles son las 5 películas más populares de cada género (considerando el número total de votos)?

SELECT title, genre FROM "IMDB" as im
LEFT JOIN genre as gen on im."Movie_id" = gen."Movie_id"
GROUP BY genre
ORDER BY "TotalVotes" DESC
LIMIT 5;

SELECT title, genre, "TotalVotes"
FROM (
    SELECT title, genre, "TotalVotes",
           ROW_NUMBER() OVER (PARTITION BY genre ORDER BY "TotalVotes" DESC) as rn
    FROM "IMDB" as im
    LEFT JOIN genre as gen on im."Movie_id" = gen."Movie_id"
) as subquery
WHERE rn <= 5
ORDER BY genre, "TotalVotes" DESC;

-- * ¿Cuál es el promedio de presupuesto de las películas de animación comparado con las de acción?
--!Falta que solo imprima Animacion y Accion, pero lo hare en Python
SELECT avg("IM"."Budget") as"Promedio Por Genero", gen.genre FROM "IMDB" as IM
INNER JOIN genre as gen on IM."Movie_id" = gen."Movie_id"
GROUP BY gen.genre
-- HAVING gen.genre ='Animation';

-- * ¿Qué género tiene la mayor proporción de películas con una calificación superior a 8?
SELECT genre, count(*) as 'numero de peliculas' FROM "IMDB" as IM
INNER JOIN "genre" as gen on "IM"."Movie_id" = "gen"."Movie_id"
WHERE "Rating" > 8
GROUP BY genre;


-- * ¿Qué porcentaje de las películas recuperan su inversión inicial (es decir, la recaudación mundial es mayor al presupuesto)?

SELECT  count(*) as "Cantidad de Peliculas con Beneficios" FROM "IMDB" as IM
LEFT JOIN earning as ear ON IM."Movie_id" = ear."Movie_id" 
WHERE ear."Worldwide" > IM."Budget";


--* ¿Cuáles son las películas que tienen un rating superior al promedio de rating de todas las películas?

SELECT title, "Rating" FROM "IMDB"
WHERE "Rating" > (SELECT AVG("Rating") FROM "IMDB");



-- * ¿Cuál es la posición de cada película en términos de recaudación mundial dentro de su género?

SELECT title FROM "IMDB" as IM
LEFT JOIN earning as ear on IM."Movie_id" = ear."Movie_id"
LEFT JOIN genre as gen on  "IM"."Movie_id" = gen."Movie_id"
WHERE gen.genre = 'Action'
ORDER BY ear."Worldwide" DESC;
-- * ¿Cuál es la posición de cada película en términos de recaudación mundial dentro de su género?
