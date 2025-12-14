"""
Student Academic Performance Analysis System
Author: (OLAYIWOLA OLAMIDE SCOTT)
Course: GSE301
"""

# ====================================
# PART 1: DATA COLLECTION AND STORAGE
# ====================================

# Fixed department information (tuple)
department_info = ("Religion Department", "Faculty of Technology", 2025)

# Unique courses offered (set)
unique_courses = {
    "Python", "Statistics", "Data Science",
    "Algorithms", "Networking", "AI"
}

# Student profiles stored as dictionaries
students = [
    {
        "name": "Rasheed Fatia",
        "matric": "23/60AC389",
        "age": 22,
        "cgpa": 4.81,
        "is_active": True,
        "courses": ["Python", "Statistics", "Data Science"],
        "grades": {"Python": "A", "Statistics": "A", "Data Science": "A"},
        "outstanding_courses": 0
    },
    {
        "name": "Yusuf Adeoye",
        "matric": "23/70JC093",
        "age": 23,
        "cgpa": 3.45,
        "is_active": True,
        "courses": ["Python", "Algorithms"],
        "grades": {"Python": "B", "Algorithms": "C"},
        "outstanding_courses": 0
    },
    {
        "name": "Moses Oyedele",
        "matric": "23/40BC112",
        "age": 21,
        "cgpa": 2.98,
        "is_active": True,
        "courses": ["Networking", "Statistics"],
        "grades": {"Networking": "C", "Statistics": "B"},
        "outstanding_courses": 1
    },
    {
        "name": "Timi Abidoye",
        "matric": "23/90EC221",
        "age": 24,
        "cgpa": 4.12,
        "is_active": True,
        "courses": ["AI", "Python"],
        "grades": {"AI": "A", "Python": "A"},
        "outstanding_courses": 0
    },
    {
        "name": "Nimah Nina",
        "matric": "23/11AC552",
        "age": 20,
        "cgpa": 2.40,
        "is_active": False,
        "courses": ["Statistics"],
        "grades": {"Statistics": "D"},
        "outstanding_courses": 2
    }
]


# ==================================
# PART 2: DATA PROCESSING AND LOGIC
# ==================================

def score_to_grade(score: int) -> str:
    """Convert score (0–100) to letter grade"""
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    match grade:
        case "A":
            print("Excellent performance!")
        case "B":
            print("Very good.")
        case "C":
            print("Good effort.")
        case "D":
            print("Fair result.")
        case "E":
            print("Poor performance.")
        case "F":
            print("Failed. Needs improvement.")

    return grade


def validate_user_input():
    """Type conversion and validation using try-except"""
    try:
        age = int(input("Enter age: "))
        cgpa = float(input("Enter CGPA: "))

        if not (16 <= age <= 40):
            raise ValueError("Age must be between 16 and 40.")

        if not (0.0 <= cgpa <= 5.0):
            raise ValueError("CGPA must be between 0.0 and 5.0.")

        return age, cgpa

    except ValueError as error:
        print("Invalid input:", error)
        return None, None


# ===============================
# PART 3: ANALYSIS AND REPORTING
# ===============================

# List slicing operations
assignment_scores = [45, 67, 89, 90, 55, 72, 81, 60, 77, 68]

top_3 = assignment_scores[:3]
last_5 = assignment_scores[-5:]
every_other = assignment_scores[::2]

# Set operations
set_pass = {"Rasheed Fatia", "Yusuf Adeoye", "Timi Abidoye"}
set_merit = {"Rasheed Fatia", "Timi Abidoye"}

passed_and_merit = set_pass & set_merit
all_students = set_pass | set_merit
passed_not_merit = set_pass - set_merit


# ===============================
# PART 4: INTERACTIVE MENU SYSTEM
# ===============================

def view_students():
    print("\nList of Students:")
    for index, student in enumerate(students, start=1):
        print(f"{index}. {student['name']}")


def add_student():
    print("\nAdd New Student")
    name = input("Enter name: ")
    matric = input("Enter matric number: ")

    age, cgpa = validate_user_input()
    if age is None:
        return

    is_active = input("Is the student active (yes/no): ").lower() == "yes"
    courses = input("Enter courses (comma separated): ").split(",")

    new_student = {
        "name": name,
        "matric": matric,
        "age": age,
        "cgpa": cgpa,
        "is_active": is_active,
        "courses": [course.strip() for course in courses],
        "grades": {},
        "outstanding_courses": 0
    }

    students.append(new_student)
    print("Student record added successfully.")


def check_eligibility():
    name = input("Enter student name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            eligible = (
                student["cgpa"] >= 2.5 and
                student["outstanding_courses"] == 0 and
                student["is_active"]
            )

            print("\nChecking eligibility...")
            print(f"Matric Number: {student['matric']}")
            print(f"CGPA: {student['cgpa']}")
            print(f"Outstanding Courses: {student['outstanding_courses']}")
            print(f"Active Status: {student['is_active']}")

            if eligible:
                print(f"{student['name']} is eligible for graduation.")
            else:
                print(f"{student['name']} is NOT eligible for graduation.")
            return

    print("Student not found.")


def top_performer():
    top_student = max(students, key=lambda x: x["cgpa"])
    print("\nTop Performer:")
    print(f"Name: {top_student['name']}")
    print(f"Matric: {top_student['matric']}")
    print(f"CGPA: {top_student['cgpa']}")
    print(f"Courses: {top_student['courses']}")


def menu():
    print("=" * 45)
    print("   Student Academic Performance System")
    print("=" * 45)
    print(f"{len(students)} student profiles loaded successfully.")

    while True:
        print("\nMenu Options")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check eligibility for graduation")
        print("4. Find top performer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                view_students()
            case "2":
                add_student()
            case "3":
                check_eligibility()
            case "4":
                top_performer()
            case "5":
                print("Exiting the system...\nGoodbye!")
                break
            case _:
                print("Invalid option. Try again.")


# ===============================
# PROGRAM ENTRY POINT
# ===============================
if __name__ == "__main__":
    menu()
