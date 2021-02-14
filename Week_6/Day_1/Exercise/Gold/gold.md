1. Create a database named bootcamp.

2. Create a table students.
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        fname VARCHAR (50) NOT NULL,
        lname VARCHAR (100) NOT NULL,
        dob DATE NOT NULL
    )


3. (INSERT 1+2) Add the columns: id, last_name, first_name, birth_date.
The id has to be auto_incremented.

    INSERT INTO students (fname, lname, dob)
    VALUES
    ('Marc', 'Benichou', '1998-11-02'),
    ('Yoan', 'Cohen', '2010-12-03'),
    ('Lea', 'Benichou', '1987-07-27'),
    ('Amelia', 'Dux', '1996-04-07'),
    ('David', 'Grez', '2003-06-14'),
    ('Omer', 'Simposin', '1980-10-03')

4. SELECT
    1. Fetch all the data from the table.
        SELECT * FROM students

    2. Fetch all the students first_name and last_name.
        SELECT fname, lname FROM students

    3. For the following questions, only fetch the first_name and last_name of the students.
        1. Fetch the student which id is equal to 2.
            SELECT * FROM students WHERE id=2
        
        2. Fetch the student with the last_name Benichou AND the first_name Marc.
            SELECT * FROM students WHERE lname='Benichou' AND fname='Marc'

        3. Fetch the students with the last_name Benichou OR the first_name Marc.
            SELECT * FROM students WHERE lname='Benichou' OR fname='Marc'

        4. Check the difference between the request 2 and 3.
            ex. 3 returns student where lname and fname match request
            ex. 4 returns student where either lname or fname match request

        5. Fetch the students which first_name contains the letter a.
            SELECT * FROM students WHERE fname LIKE '%a%'

        6. Fetch the students which first_name starts with the letter a.
            SELECT * FROM students WHERE fname LIKE 'A%'

        7. Fetch the students which first_name ends with the letter a.
            SELECT * FROM students WHERE fname LIKE '%a'

        8. Fetch the students where the second to last letter of the first_name is a
            SELECT * FROM students WHERE fname LIKE '%a_'
        
        9. Fetch the students which the id are 1 AND 3
            SELECT * FROM students WHERE id=1 OR id=3
        

    
    4. Fetch the students, which birth_date is equal or after the 1/01/2000. (show their first_name, last_name and birth_date)
        SELECT fname, lname, dob FROM students WHERE dob >='2000-01-01'
