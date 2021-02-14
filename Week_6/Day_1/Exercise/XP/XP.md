Create two tables: items and customers:

CREATE TABLE item(
 id SERIAL PRIMARY KEY,
 item VARCHAR (50) NOT NULL,
 price SMALLINT
)

CREATE TABLE customers(
 id SERIAL PRIMARY KEY,
 fname VARCHAR (50) NOT NULL,
 lname VARCHAR (100) NOT NULL,
)


1. Add the following new items to the public.items table:
INSERT INTO item (item, price)
VALUES
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80)


2. Add the following new items to the public.customers table:
INSERT INTO customers (fname, lname)
VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson')


3. Use SQL to get the following data from the database:
    1. All the items
        SELECT * FROM item
    2. SELECT * FROM item WHERE price >80
    3. SELECT * FROM item WHERE price <300
    4. SELECT * FROM customers WHERE lname='Smith' (result: empty record)
    5. SELECT * FROM customers WHERE lname='Jones'
    6. SELECT * FROM customers WHERE lname != 'Scott'