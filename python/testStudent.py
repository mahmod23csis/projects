from modStudentV1 import *

def main():
    s1 = Student("Jones", "Chemistry", 3.4)
    print(s1)

    id = s1.getID()
    print("ID is ", id)
    print("Number of students: ", Student.getNumStudents())

    s2 = Student("Miller", "Math", 3.0)
    print(s2)
    print("Number of students: ", Student.getNumStudents())

    name = s2.getName()
    major = s1.getMajor()
    gpa = s1.getGPA()
    print(name, major, gpa)

    s2.setName("Ahmad")
    s2.setMajor("CSIS")
    s2.setGPA(4.0)
    print(s2)

main()
