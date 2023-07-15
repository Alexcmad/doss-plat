"""Description: Create a student management system that allows users to perform basic operations such as adding,
retrieving, updating, and deleting student records. The program should utilize various Python concepts,
including variables, data types, lists, tuples, sets, dictionaries, conditionals, type casting, exceptions,
functions, and built-in functions.

Requirements:

The program should provide a menu-driven interface with the following options:
a. Add a new student record
b. Retrieve a student record by ID
c. Update a student record
d. Delete a student record
e. Display all student records
f. Exit the program

Each student record should contain the following information:

- Student ID (integer)
- Name (string)
- Age (integer)
- Grade (float)

Use appropriate data structures to store the student records. For example, you can use a list of dictionaries,
where each dictionary represents a student record.

Implement error handling to handle potential exceptions such as invalid input or non-existent student IDs.

Implement input validation to ensure that the user enters the correct data type for each field (e.g., integer for ID,
string for name).

Provide appropriate messages to inform the user of the outcome of each operation (e.g., "Student record added
successfully," "Student record not found," etc.).

Use built-in functions such as len(), input(), str(), int(), etc., as needed throughout the program.
"""

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


if __name__ == "__main__":
    main()
