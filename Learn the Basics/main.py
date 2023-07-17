students_list = []


class Student:
    school = "Crawsis"

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
    """
    alex = Student(name="alexander", age=20, grade=2, ID=69)
    print(alex == 69)
    doss = Student(name="Doss", age=18, grade=15, ID=20031)"""
    # comment
    # second comment
    add_student()
    input("Press Enter to Continue...")
    choice=input("\nEnter 1 to add another student\nEnter 0 to exit \n" )
    choice=int(choice)

    if choice==1:
        add_student()

    else:
        exit()

def add_student():
    student_name=input("Enter Student Name ")
    student_age=int(input("Enter Student Age "))
    student_grade=float(input("Enter Student Grade "))
    student_id=int(input("Enter Student Id "))

    new_student=Student(name=student_name,age=student_age,grade=student_grade,ID=student_id )
    students_list.append(new_student)

if __name__ == "__main__":
    main()

def get_student():
    student_id = input("What is the id of the student you want to find?")

    for student in students_list:
        if student_id == student.ID:
            print(student.name,student.age,student.grade,student.id)
            input("press enter to continue")
            return student

    print("student not on record")
    input("press enter to continue")






def print_student_info(student):
    print(student.name, student.age, student.grade, student.id)









