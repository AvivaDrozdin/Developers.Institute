EXERCISE 1

1. Find out how many films there are for each rating
    SELECT rating, count(rating) FROM film GROUP BY rating

2. Get a list of all the movies that have a rating of G or PG-13
    1. Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
    	 SELECT title FROM film 
        WHERE rating IN ('G', 'PG-13') AND length < 120 AND rental_rate < 3.0 
        ORDER BY title ASC

3. Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
        UPDATE address SET first_name='Aviva', last_name='Drozdin' WHERE customer_id=9

4. 


EXERCISE 2
1. UPDATE:
    1. Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same  birth_date. Update both their birth_date to 02/11/1998.
        UPDATE students SET dob='1998-11-02' WHERE lname='Benichou'
    
    2. Change the last_name of David from ‘Grez’ to ‘Guez’.
        UPDATE students SET lname='Guez' WHERE lname='Grez'

2. DELETE Lea
    SELECT * FROM students WHERE fname='Lea';
    DELETE FROM students WHERE id=3

3. COUNT
    1. Count how many students are in the table .
        SELECT count(*) FROM students
    
    2. Count how many students were born after 1/01/2000.
        SELECT count(*) FROM students WHERE dob > '2000-01-01'

4. INSERT / ALTER
   1. Add a column to the table student, called math_grade.
        ALTER TABLE students ADD COLUMN math_grade SMALLINT

    2. Add the grade 80 to the student which id is 1.
        UPDATE students
        SET math_grade = 80 WHERE id =1

    3. Add the grade 90 to the students which id are 2 and 4.
        UPDATE students
        SET math_grade = 80 WHERE id =1

    4. Add the grade 40 to the student which id is 6.
        UPDATE students
        SET math_grade = 80 WHERE id=1

    5. Count how many students have a grade bigger than 83
        SELECT count(*) FROM students WHERE math_grade >83

    6. Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him the grade 70.
        INSERT INTO students (fname, lname, dob, math_grade) VALUES ('Omer', 'Simpson', '1980-10-03', 70)

SUM
SELECT sum (math_graade) FROM students

