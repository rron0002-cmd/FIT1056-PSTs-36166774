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

-find_teachers(term -> string): Finds teachers by name.

Front Desk Functions:
-find_student_by_id(student_id -> int): A new helper to find one student in the database by their exact ID. Used for enroling existing student (see option 2 via menu)

-front_desk_register(name -> string, instrument -> string): creates a new student object, stores it in student_db, increments next_student_id, and immediately enrols the student in the requested instrument.

-front_desk_enrol(student_id -> int, instrument -> string): uses find_student_by_id(student_id) to locate the student; if found, appends the instrument to their enrolled_in list, otherwise prints an error.

-front_desk_lookup(term -> string): function to search everything via find_students/find_teachers functions. test via option 3 of menu.

PST2
Files Added and implemented: pst2_main.py, Fragment2_2.py, Fragment2_3.py, Fragment2_4.py
Date last edited: 14/08/2026

Changes:
Shift from object-oriented memory into dictionary type memory storage
Store data through json file

add_teacher()

update_teacher()

remove_teacher()

remove_student()

update_student()

check_in() records attendance with timestamps.

print_student_card() generates a text badge.

PST3
Files Added and implemented: (app --> schedule.py, student.py, teacher.py, user.py) (data -->msms.json) Fragment3_3,py, main.py
Date last edited 4/09/2026

Changes:
Shift into object oriented program. Classes for student, teacher and courses as well as Schedule Manager Class with main functions

load_data()
save_data()
get_lessons_by_day()
check_in()
enrol_student_in_course()
