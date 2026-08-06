# FIT1056-PSTs-36166774
My individual FIT1056 PSTs and Python practice

PST1
Files Added and implemented: MSMS.py
Date Last edited: 7/08/2026

Data Models:
-Student: Student objects in which an ID (int), name (string) and subject enrolled in (List) is stored
-Teacher: Teacher objects in which an ID (int), name (string) and Specialty String is stored

In Memory Databases:
-student_db (type: List): global storage of all students enrolled
-teacher_db (type: List): global storage of all teachers enrolled

Core Helper Functions:
-add_teacher(name -> string, speciality -> string): adds a teacher to the database after creating it (can be tested by adding line with sample teachers e.g. add_teacher("Ms. Fret", "Guitar") and then using the lookup option in the menu)

-list_students(): Prints all students in the database (if any, otherwise prints a statement saying no students), can be tested via menu option 4.

-list_teachers(): Similar to list_students, prints all teachers in database, can be tested via menu option 5

-find_students(term -> string): Finds students by name.

-find_teachers(term -> string): Finds students by name.