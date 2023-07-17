import os

from exceptions import InvalidOptionException

students_list = []


class Student:
    school = "UA"

    def __init__(self, name: str, age: int, grade: float, ID: int):
        self.name = name
        self.age = age
        self.grade = grade
        self.ID = ID

    def print_info(self):
        print(f"Name:{self.name} | Age:{self.age} | Grade:{self.grade} | ID:{self.ID}")

    def update(self, name: str, age: str, grade: str, ID: str):
        try:
            if name:
                self.name = name
            if age:
                self.age = int(age)
            if grade:
                self.grade = float(grade)
            if ID:
                self.ID = int(ID)

            print("Student Record Updated Successfully")
        except:
            print("Error Updating Student Record")

    def __repr__(self):
        return f"{self.name}:{self.ID}:{self.age}:{self.grade}"

    def __str__(self):
        return f"Name:{self.name}, ID:{self.ID}"

    def __eq__(self, other):
        return self.ID


def main():
    function_dict = {
        1: add_student,
        2: find_student_by_id,
        3: update_student_record,
        5: print_all_records
    }

    choice = 0

    print("Welcome to the Python Roadmap School Admin System")

    def display_options():
        selection = input("What would you like to do?:\n"
                          "1) Add a student record\n"
                          "2) Get a student by ID\n"
                          "3) Update a student record by ID\n"
                          "4) Delete a student record by ID\n"
                          "5) View all student records\n"
                          "6) Exit program\n"
                          "Please enter the option you would like to choose: ")
        return selection

    try:
        choice = int(display_options())
        if choice > 6 or choice <= 0:
            raise InvalidOptionException
    except (InvalidOptionException, ValueError):
        input("Invalid Option, please try again\n"
              "Press enter to continue...")
        choice = display_options()

    chosen_function = function_dict.get(choice)
    chosen_function()
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


def add_student():
    student_name = input("Enter Student Name: ")
    student_age = int(input("Enter Student Age: "))
    student_grade = float(input("Enter Student Grade: "))
    student_id = int(input("Enter Student Id: "))

    new_student = Student(name=student_name, age=student_age, grade=student_grade, ID=student_id)
    students_list.append(new_student)


def find_student_by_id():
    student_id = input("What is the id of the student you want to find?: ")
    student = get_student(student_id)

    if student:
        print(student)

    choice = input("Press enter to continue or s to search again: ")
    if choice.lower() == "s":
        find_student_by_id()


def update_student_record():
    student_id = input("Please enter the ID of the student whose record you wish to update: ")
    student = get_student(student_id)

    if student:
        student.print_info()
        print("For the following fields enter a new value or press enter to skip")
        new_name = input("Name: ")
        new_age = input("Age: ")
        new_grade = input("Grade: ")
        new_ID = input("ID: ")
        student.update(name=new_name, age=new_age, ID=new_ID, grade=new_grade)
        enter_continue()

    choice = input("Press enter to continue or s to search again: ")
    if choice.lower() == "s":
        update_student_record()


def enter_continue():
    input("Press Enter to continue...")


def get_student(student_id: str):
    for student in students_list:
        if int(student_id) == student.ID:
            return student
    print(f"Student with ID of {student_id} not found")


def print_all_records():
    for student in students_list:
        student.print_info()
    enter_continue()


if __name__ == "__main__":
    main()
