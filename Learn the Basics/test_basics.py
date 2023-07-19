import unittest
from . import main


class TestAdmin(unittest.TestCase):
    def setUp(self) -> None:
        self.student = main.Student(name="Test Student", age=12, grade=80.3, ID=1234)

    def test_student_creation(self):
        self.assertEquals(self.student.name, "Test Student")
        self.assertEquals(self.student.age, 12)
        self.assertEquals(self.student.grade, 80.3)
        self.assertEquals(self.student.ID, 1234)

    def test_add_student(self):
        self