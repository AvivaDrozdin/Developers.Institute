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





