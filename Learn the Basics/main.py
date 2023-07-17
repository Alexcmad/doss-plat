from exceptions import InvalidOptionException

students_list = []


class Student:
    school = "UA"

    def __init__(self, name: str, age: int, grade: float, ID: int):
        self.name = name
        self.age = age
        self.grade = grade
        self.ID = ID

    def __repr__(self):
        return f"{self.name}:{self.ID}:{self.age}:{self.grade}"

    def __str__(self):
        return f"Name:{self.name}, ID:{self.ID}"

    def __eq__(self, other):
        return self.ID


def main():
    function_dict = {
        1: add_student,
        2: get_student,
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
    main()


def add_student():
    student_name = input("Enter Student Name: ")
    student_age = int(input("Enter Student Age: "))
    student_grade = float(input("Enter Student Grade: "))
    student_id = int(input("Enter Student Id: "))

    new_student = Student(name=student_name, age=student_age, grade=student_grade, ID=student_id)
    students_list.append(new_student)


def get_student():
    student_id = input("What is the id of the student you want to find?: ")
    found_student = False
    for student in students_list:
        if int(student_id) == student.ID:
            print(student.name, student.age, student.grade, student.ID)
            found_student = True
            break
    if not found_student:
        print(f"Student with ID of {student_id} not found")

    choice = input("Press enter to continue or s to search again: ")
    if choice.lower() == "s":
        get_student()


def print_student_info(student):
    print(student.name, student.age, student.grade, student.ID)


def print_all_records():
    for student in students_list:
        print_student_info(student)
    input("Press enter to continue...")


if __name__ == "__main__":
    main()
