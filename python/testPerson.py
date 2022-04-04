from modPerson import *

p1 = Person("Bob Brown")
print("Person 1: ", p1)
print("Population is now: ", Person.getPopulation())

p2 = Person("Amy Ant")
print("Person 2: ", p2)
print("Population is now: ", Person.getPopulation())

s1 = Student("Tim Top", "Biology")
s2 = Student("Gary Gray", "Art")
s3 = Student("Cal Cool", "Biology")

print("Student 1: ", s1)
print("Student 2: ", s2)
print("Student 3: ", s3)
print("Population is now: ", Person.getPopulation())

print("Number of Bio Majors: ", Student.getNumBioMajors())
