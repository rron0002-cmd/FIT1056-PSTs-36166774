import json
from app.student import StudentUser
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        # TODO: Initialize the new attendance_log attribute as an empty list.
        self.attendance_log = []
        self.next_student_id = None
        self.next_teacher_id = None
        self.next_course_id = None
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # TODO: Load students, teachers, and courses as before.
                # Load students
                self.students = [
                StudentUser(s["id"], s["name"]) for s in data.get("students", [])]
                for s, raw in zip(self.students, data.get("students", [])):
                    s.enrolled_course_ids = raw.get("enrolled_course_ids", [])

                # Load teachers
                self.teachers = [
                    TeacherUser(t["id"], t["name"], t["speciality"]) for t in data.get("teachers", [])
                ]

                # Load courses
                self.courses = []
                for c in data.get("courses", []):
                    course = Course(c["id"], c["name"], c["instrument"], c["teacher_id"])
                    course.enrolled_student_ids = c.get("enrolled_student_ids", [])
                    course.lessons = c.get("lessons", [])
                    self.courses.append(course)

                # TODO: Correctly load the attendance log.
                # Use .get() with a default empty list to prevent errors if the key doesn't exist.
                self.attendance_log = data.get("attendance", [])
                self.next_student_id = data.get("next_student_id", len(self.students) + 1)
                self.next_teacher_id = data.get("next_teacher_id", len(self.teachers) + 1)
                self.next_course_id = data.get("next_course_id", len(self.courses) + 1)
                
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
    
    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # TODO: Create a 'data_to_save' dictionary.
        data_to_save = {
            "students": [s.__dict__ for s in self.students],
            "teachers": [t.__dict__ for t in self.teachers],
            "courses": [c.__dict__ for c in self.courses],
            # TODO: Add the attendance_log to the dictionary to be saved.
            # Since it's already a list of dicts, no conversion is needed.
            "attendance": self.attendance_log,
            # ... (next_id counters) ...
            "next_student_id": self.next_student_id,
            "next_teacher_id": self.next_teacher_id,
            "next_course_id": self.next_course_id
        }
        # TODO: Write 'data_to_save' to the JSON file.
        with open(self.data_path, 'w') as f:
            json.dump(data_to_save, f, indent=4)