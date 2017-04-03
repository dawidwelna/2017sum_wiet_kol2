#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


import math


class Student:
	
	def __init__(self, name, surname, id):
		self.name = name
		self.surname = surname
		self.id = id
	
	def create_student(self, name, surname, id):
		self.name = name
		self.surname = surname
		self.id = id

	def speak(self):
		print "Hello! I am {} {}, my id number is {}".format(self.name, self.surname, self.id)
		
		

class Subject(Student):
	
	def __init__(self, subject_name, teacher):
		self.subject_name = subject_name
		self.teacher = teacher
		
	def speak(self):
		print "This subject is called {}".format(self.subject_name)

		
class Grades(Subject):
	
	attendance = 0
	total_attendance = 14
	
	def __init__(self, grade, lesson_number):
		self.lesson_number = lesson_number
		self.grade = grade
	
	def addGrade(self, grade, lesson_number):
		self.lesson_number = lesson_number
		self.grade = grade
		
	def count_attendance(self):
		self.attendance = self.attendance + 1
		
		
		
		
def main():
	s1 = Student('Andrzej', 'Rdad', 1)
	s1.speak()

	sub1 = Subject('Literature', 'Arthur C. Doyle')
	sub1.speak()
	
	
main()