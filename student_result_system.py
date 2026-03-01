import json

# -------------------- CLASS DEFINITION (OOP) --------------------
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        try:
            if self.marks >= 90:
                return "A+"
            elif self.marks >= 75:
                return "A"
            elif self.marks >= 60:
                return "B"
            elif self.marks >= 50:
                return "C"
            else:
                return "Fail"
        except Exception as e:
            print("Error in grade calculation:", e)
            return "N/A"

# -------------------- FILE HANDLING --------------------
FILE_NAME = "students.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Create new file if not exists
    except json.JSONDecodeError:
        return []  # Empty if corrupted

def save_data(data):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error saving data:", e)

# -------------------- FUNCTIONS --------------------
def add_student():
    try:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks (0-100): "))

        student = Student(roll, name, marks)

        data = load_data()
        data.append({
            "roll": student.roll,
            "name": student.name,
            "marks": student.marks,
            "grade": student.grade
        })
        save_data(data)

        print("\nStudent added successfully!\n")
    except ValueError:
        print("Invalid input! Marks must be a number.")
    except Exception as e:
        print("Error:", e)

def display_all_students():
    data = load_data()
    if not data:
        print("\nNo student records found.\n")
        return

    print("\n--- All Student Records ---")
    for st in data:
        print(f"Roll: {st['roll']}  |  Name: {st['name']}  |  Marks: {st['marks']}  |  Grade: {st['grade']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")

    data = load_data()
    found = False

    for st in data:
        if st["roll"] == roll:
            print("\n--- Student Found ---")
            print(f"Roll: {st['roll']}")
            print(f"Name: {st['name']}")
            print(f"Marks: {st['marks']}")
            print(f"Grade: {st['grade']}\n")
            found = True
            break

    if not found:
        print("\nNo student found with this roll number.\n")

# -------------------- MENU-DRIVEN SYSTEM --------------------
def menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Roll Number")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# -------------------- MAIN --------------------
if __name__ == "__main__":
    menu()
