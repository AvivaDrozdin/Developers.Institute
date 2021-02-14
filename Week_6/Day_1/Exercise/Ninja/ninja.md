For the following questions, you have to fetch the first_name, last_name and birth_date of the students.
    SELECT fname, lname, dob FROM students

1.  Fetch the first four students. You have to order the answer by last_name alphabetically.
    SELECT fname, lname, dob FROM students ORDER BY fname DESC LIMIT 4

2. Fetch the birth_date of the youngest student.
    SELECT dob FROM students ORDER BY dob DESC LIMIT 1

3. Fetch three students, skipping the first two students.
    SELECT fname, lname, dob FROM students OFFSET 2