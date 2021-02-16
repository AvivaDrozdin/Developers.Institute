1. 
    SELECT name FROM language

2. 
    1. 
    SELECT language.name, film.title, film.description 
    FROM film
    LEFT JOIN language
    ON language.language_id = film.language_id

    2. 
    SELECT language.name, film.title, film.description 
    FROM film
    RIGHT JOIN language
    ON language.language_id = film.language_id
    ORDER BY language.name DESC
    # empty languages: Mandarin, Japanese, Italian, German, French

3. 
    # add new table movie
    CREATE TABLE new_film(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
    );

    # add new table reviews
    CREATE TABLE customer_review(
    id SERIAL PRIMARY KEY,
    film_id SMALLINT REFERENCES new_film(id)
    ON DELETE CASCADE,
    language_id SMALLINT,
    FOREIGN KEY (language_id) REFERENCES language(language_id),
    title VARCHAR(50),
    score SMALLINT,
    review_text TEXT,
    last_update DATE
    )

    # add movies to new_movie
    INSERT INTO new_film (name)
    VALUES
    ('Jaws'),
    ('Titanic'),
    ('22 Jump Street')


5. 
    INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
    VALUES
    (1, 1, 'Jaws', 6, 'Unrealistically large Shark', '2021-02-16'),
    (2, 1, 'Titanic', 8, 'Alright', '2021-02-16'),
    (3, 1, '22 Jump Street', 6, 'Arent they too old for collage?','2021-02-16')

6. 
    DELETE  FROM new_film WHERE id=2


EXERCISE 2.

1. UPDATE customer_review SET language_id=5 WHERE film_id=1


2.  Foreign Keys: store_id, address_id (3)
    To insert into a table with multiple keys we need to know the ID of each of the individual values


3. DROP TABLE customer_review 
    # No extra step, dependencies all on foreign key and not on ON DELETE


4. SELECT count(rental_date) - count(return_date) FROM rental


5.  SELECT  rental.rental_id, inventory.film_id, film.rental_rate
    FROM (inventory JOIN rental ON inventory.inventory_id = rental.inventory_id)
    JOIN film
    ON film.film_id = inventory.film_id
    ORDER BY rental_rate DESC
    WHERE return_date IS NULL
    LIMIT 30

6.  
    1.  SELECT film.title
        FROM (actor JOIN film_actor ON actor.actor_id = film_actor.actor_id)
        JOIN film ON film.film_id = film_actor.film_id
        WHERE film.description LIKE '%Sumo%'
        AND actor.first_name = 'Penelope'
        AND actor.last_name = 'Monroe'

    
    2. 
        SELECT film.title 
        FROM category
        INNER JOIN film_category
        ON category.category_id = film_category.category_id
        INNER JOIN film
        ON film.film_id = film_category.film_id
        WHERE rating = 'R'
        AND length < 60
        AND category.category_id = 6

    
    3.  SELECT film.title 
        FROM film
        INNER JOIN inventory
        ON film.film_id = inventory.film_id
        INNER JOIN rental
        ON rental.inventory_id = inventory.inventory_id
        INNER JOIN customer
        ON rental.customer_id = customer.customer_id
        WHERE first_name = 'Matthew'
        AND last_name = 'Mahan'
        AND rental_rate > 4
        AND rental.return_date BETWEEN '28/07/2005' AND '01/08/2005'


    4. 
        SELECT film.title, film.replacement_cost 
        FROM film
        INNER JOIN inventory
        ON film.film_id = inventory.film_id
        INNER JOIN rental
        ON rental.inventory_id = inventory.inventory_id
        INNER JOIN customer
        ON rental.customer_id = customer.customer_id
        WHERE customer.first_name = 'Matthew'
        AND customer.last_name = 'Mahan'
        OR film.title LIKE '%Boat%' 
        OR film.description LIKE '%Boat%'
        ORDER BY film.replacement_cost DESC LIMIT 1




 




