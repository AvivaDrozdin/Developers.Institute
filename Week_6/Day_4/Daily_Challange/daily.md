CREATE TABLE items(
id SERIAL PRIMARY KEY,
item VARCHAR(50)NOT NULL,
price SMALLINT NOT NULL 	
)

insert into items(item,price)
values
('Bag',700),
('Dress',150),
('Shirt',50),
('Jeans',75),
('Shoes',400);


CREATE TABLE purchase(
id SERIAL PRIMARY KEY,
price SMALLINT			
)


CREATE TABLE items_purchase(
items SMALLINT REFERENCES items(id) ON DELETE CASCADE,
purchase SMALLINT REFERENCES purchase(id) ON DELETE CASCADE
)
INSERT INTO items_purchase (purchase,items)
VALUES
(1,1),
(1,2),
(1,3),
(2,4),
(2,5),
(3,1),
(3,2),
(3,3),
(3,4),
(3,5),
(4,4),
(5,1),
(5,5)

CREATE FUNCTION purchase_price(ord integer)
RETURNS integer AS "Full Price"
BEGIN
return(
select sum(price) from items
join items_purchase
on items.id = items_purchase.items
where orders= ord);  
END;


SELECT * FROM purchase_price(4)

