from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

class Assessment(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def grade(self):
        pass

class Quiz(Assessment):
    def grade(self):
        print(f"Grading quiz: {self.title} automatically.")

class Assignment(Assessment):
    def grade(self):
        print(f"Grading assignment: {self.title} manually.")

T = TypeVar('T', bound=Assessment)

class Course(Generic[T]):
    def __init__(self, name: str):
        self.name = name
        self.assessments: List[T] = []

    def add_assessment(self, assessment: T):
        self.assessments.append(assessment)

    def grade_all(self):
        for assessment in self.assessments:
            assessment.grade()

C = TypeVar('C', bound=Course)

# user classes
class User():
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email

    def set_name(self, name:str):
        self.name = name

class Admin(User):
    def __init__(self, employee_id:str):
        self.employee_id = employee_id

    def add_course(self, course: C):
        self.courses.append(course)

    def del_course(self, course: C):
        self.courses.remove(course)

    def list_courses(self, course: C):
        for course in self.courses:
            print(course)


class Instructor(User, Generic[C]):
    def __init__(self):
        self.courses: List[C] = []

    def add_course(self, course: C):
        self.courses.append(course)

    def del_course(self, course: C):
        self.courses.remove(course)

    def list_courses(self, course: C):
        for course in self.courses:
            print(course)

class Student(User):
    def __init__(self, student_id:str):
        self.student_id = student_id

#Complete your main function here
if __name__ == "__main__":
    course = Course[Assessment]("Computer Science 1")

    quiz1 = Quiz("Quiz 1")
    assignment1 = Assignment("Assignment 1")

    course.add_assessment(quiz1)
    course.add_assessment(assignment1)

    course.grade_all()


    instructor = Instructor()


    instructor.add_course("Introduction to Python")
    instructor.add_course("Data Structures and Algorithms")
    instructor.list_courses(course)

