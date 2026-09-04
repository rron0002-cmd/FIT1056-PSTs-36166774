# main.py - The View Layer
from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """Displays a pretty table of all lessons on a given day."""
    print(f"\n--- Daily Roster for {day} ---")
    # Notice: This code does not need to change. It doesn't care where the Course class lives.
    # It only talks to the manager.
    # TODO: Call a method on the manager to get the day's lessons and print them.
    lessons = manager.get_lessons_by_day(day)

    if not lessons:
        print("No lessons scheduled for this day.")
        return

    for lesson in lessons:
        course = manager.find_course_by_id(lesson["course_id"])
        teacher = manager.find_teacher_by_id(course.teacher_id)
        print(f"{lesson['start_time']:>8} | {course.name:<25} | {teacher.name:<20} | Room: {lesson['room']}")


def switch_course(manager, student_id, from_course_id, to_course_id):
    # TODO: Implement the logic to switch a student by calling methods on the manager.
    student = manager.find_student_by_id(student_id)
    if not student:
        print("Student not found.")
        return

    success = manager.switch_student_course(student_id, from_course_id, to_course_id)
    if success:
        print(f"Student {student.name} switched from course {from_course_id} to {to_course_id}.")
    else:
        print("Switch failed. Check course IDs or enrolment status.")

def main():
    """Main function to run the MSMS application."""
    manager = ScheduleManager()  # Create ONE instance of the application brain.

    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1. View Daily Roster")
        print("2. Switch Student Course")
        print("3. List All students")
        print("4. List All Teachers")
        print("5. Check in Student")
        print("6. Find Student By ID")
        print("7. Find Course By ID")
        print("8. Find Teacher By ID")
        print("9. Remove Student")
        print("10. Enrol Student")
        print("q. Quit")

        choice = input("Enter choice: ").strip().lower()

        if choice == '1':
            day = input("Enter day (e.g., Monday): ").strip()
            front_desk_daily_roster(manager, day)

        elif choice == '2':
            try:
                student_id = int(input("Enter student ID: "))
                from_course_id = int(input("Enter current course ID: "))
                to_course_id = int(input("Enter new course ID: "))
                switch_course(manager, student_id, from_course_id, to_course_id)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == '3':
            print("\n--- All Students ---")
            for student in manager.list_students():
                print(f"ID: {student.id} | Name: {student.name} | Enrolled Courses: {student.enrolled_course_ids}")

        elif choice == '4':
            print("\n--- All Teachers ---")
            for teacher in manager.list_teachers():
                print(f"ID: {teacher.id} | Name: {teacher.name} | Speciality: {teacher.speciality}")

        elif choice == '5':
            try:
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                if manager.check_in(student_id, course_id):
                    print("Student checked in successfully.")
                else:
                    print("Check-in failed. Invalid IDs.")
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == '6':
            try:
                student_id = int(input("Enter student ID: "))
                student = manager.find_student_by_id(student_id)
                print(f"Found: {student.name}" if student else "Student not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '7':
            try:
                course_id = int(input("Enter course ID: "))
                course = manager.find_course_by_id(course_id)
                print(f"Found: {course.name}" if course else "Course not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '8':
            try:
                teacher_id = int(input("Enter teacher ID: "))
                teacher = manager.find_teacher_by_id(teacher_id)
                print(f"Found: {teacher.name}" if teacher else "Teacher not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '9':
            try:
                student_id = int(input("Enter student ID to remove: "))
                if manager.remove_student(student_id):
                    print("Student removed successfully.")
                else:
                    print("Student not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == '10':
            try:
                student_id = int(input("Enter student ID: "))
                course_id = int(input("Enter course ID: "))
                message = manager.enrol_student_in_course(student_id, course_id)
                print(message)
            except ValueError:
                print("Invalid input. Please enter numeric IDs.")

        elif choice == 'q':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()