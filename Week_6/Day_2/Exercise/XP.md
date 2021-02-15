EXERCISE 1

1. Use SQL to get the following from the database:
    1. All items, ordered by price (lowest to highest).
        SELECT * FROM item ORDER BY price ASC
    
    2. Items with a price above 80 (80 included), ordered by price (highest to lowest).
        SELECT * FROM item WHERE price >= 80 ORDER BY price DESC
    
    3. The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
        SELECT fname, lname FROM customers ORDER BY first_name ASC LIMIT 3

    4. All last names (no other columns!), in reverse alphabetical order (Z-A)
        SELECT lname FROM customers ORDER BY lname DESC
    

2. Create a table named purchases. It should have 2 columns : customer_id and item_id. These columns are references from the tables customers and items. Edit the data of the purchases table:
    CREATE TABLE purchases (
        customer_id SMALLINT,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
        item_id SMALLINT,
        FOREIGN KEY (item_id) REFERENCES 
        )

    1. Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
        INSERT INTO purchases (customer_id)
        VALUES
        (1)
        # adds customer id to table and leaves item id at null

    2. Add 5 rows which reference existing customers and items.
        INSERT INTO purchases (customer_id, item_id)
        VALUES
        (2, 3),
        (2, 4),
        (3, 3),
        (3, 1),
        (1, 2)

3. Use SQL to get the following from the database
    1. All purchases. Is this information useful to us?
        SELECT * FROM purchases
        # not usefull, as we don't know who the customers are and what they have purchased, only their id's

    2. All purchases, joining with the customers table.
        SELECT * 
        FROM customers
        INNER JOIN purchases
        ON customers.id = purchases.customer_id

    3. Purchases of the customer with the ID equal to 4.
        SELECT * FROM purchases WHERE customer_id=4

    4. Purchases of the customer with the ID equal to 4.
        SELECT * FROM purchases WHERE item_id IN (1,2)

4. Create a purchase for Scott Scott – he bought a hard drive.
    INSERT INTO item (item, price)
    VALUES
    ('Harddrive', 25);

    INSERT INTO purchases (customer_id, item_id)
    VALUES
    (2,4)

5. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
    SELECT customers.fname, customers.lname, item.item 
    FROM purchases 
    INNER JOIN item
    ON item.id = purchases.item_id
    INNER JOIN customers
    ON customers.id = purchases.customer_id

EXERCISE 2
1. done
2. 
    1. Write a query to select all the columns from the table “customer” in the database named dvdrental.
        SELECT * FROM customer
    
    2. Write a query to display the names (first_name, last_name) using an alias named “full_name”.
        SELECT first_name || ' ' || last_name AS full_name FROM customer

    3. You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.
        SELECT create_date FROM customer GROUP BY create_date

    4. Write a query to get the details of all customers from the customer table in descending order by their first name.
        SELECT * FROM customer ORDER BY first_name DESC

    5. Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
        SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC

    6. Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.
        SELECT address, district, phone FROM address WHERE district ='Texas'

    7. Write a query to retrieve the details of the movies with the id 15 and 150.
        SELECT * FROM film WHERE film_id in (15, 150)

    8. Pick your favorite movie. Write a query to see if the rental shop owns it. Write a query to get the film ID, the title, the description, the length and the rental rate from the film table for your movie title.
        SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE '_atch me if you can';

    9. Didn’t find it ? Maybe you made a mistake in the name. Write a query to get the film ID, the title, the description, the length and the rental rate from the “film” table for all the movies starting with the two first letters of your movie.
        SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'Ca%'

    10. You want to have a choice between ten propositions of movies and you want the cheapest ones. Write a query to find the 10th cheapest movies.
        SELECT title FROM film ORDER BY rental_rate ASC LIMIT 10

    11. You are not satisfied with the results. Write a query to find the 10th next cheapest movies.
        SELECT title FROM film ORDER BY rental_rate ASC OFFSET 10 FETCH FIRST 10 ROW ONLY

    12. Write a query to join the data of the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by his id (from 1 to…).
        SELECT customer.customer_id, customer.first_name, customer.last_name, payment.payment_date, payment.amount
        FROM payment
        INNER JOIN customer
        ON customer.customer_id = payment.customer_id
        ORDER BY customer.customer_id ASC

    13. You need to check your inventory. Write a query to get all the  movies which are not in the inventory.
        SELECT film.title, f
        FROM film
        INNER JOIN inventory
        ON film.film_id = inventory.film_id
        WHERE film.film_id NOT inventory.film_id
        # not working

    14. Write a query to find which city is in which country.
        SELECT city.city, country.country
        FROM city
        INNER JOIN country
        ON city.country_id = country.country_id

    15. Bonus :You want to be assured of the performance of your sellers. Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff who sold them the dvd.
        SELECT staff.staff_id, customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
        FROM customer
        INNER JOIN staff
        ON customer.store_id = staff.store_id
        INNER JOIN payment
        ON customer.customer_id = payment.customer_id



