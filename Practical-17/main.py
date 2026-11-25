print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
class University:
    def __init__ (self,university_name):
        self.university_name = university_name
class Student:
    def __init__ (self,name,enrollment_no,department):
        self.name = name
        self.enrollment_no = enrollment_no
        self.department = department
    def display(self):
        print("Student Name:",self.name)
        print("Entollment_No:",self.enrollment_no)
        print("Department:",self.department)
univ = University("Marwadi University")
stud = Student("Rajveer Vaya",92600565002,"FoCa")
print("University:",univ.university_name)
stud.display()
