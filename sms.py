import csv
import os

FILENAME = "students.csv"
FIELDS = ["StudentID", "Name", "Age", "Course", "Grade"]

# Ensure file exists with headers
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

# Add a new student
def add_student():
    student = {}
    student["StudentID"] = input("Enter Student ID: ")
    student["Name"] = input("Enter Name: ")
    student["Age"] = input("Enter Age: ")
    student["Course"] = input("Enter Course: ")
    student["Grade"] = input("Enter Grade: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(student)
    print("Student added successfully!\n")

# View all students
def view_all():
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    print()

# Search student by ID
def search_by_id():
    student_id = input("Enter Student ID to search: ")
    found = False
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                print(row)
                found = True
    if not found:
        print("No student found with this ID.")
    print()

# Update grade of a student
def update_grade():
    student_id = input("Enter Student ID to update grade: ")
    updated = False
    rows = []
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                row["Grade"] = input("Enter new Grade: ")
                updated = True
            rows.append(row)

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    if updated:
        print("Grade updated successfully!\n")
    else:
        print("Student not found.\n")

# Delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    deleted = False
    rows = []
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] != student_id:
                rows.append(row)
            else:
                deleted = True

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    if deleted:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Student ID")
        print("4. Update Grade")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_by_id()
        elif choice == "4":
            update_grade()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    menu()
