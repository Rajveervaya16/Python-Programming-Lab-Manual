print("M.sc. (CS&CL)Semester 1")
print("Enrollment No:92600565002")
# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a generic sound.")
# Child Class overriding the speak method
class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof Woof!")
# Main Execution
print("Student Enrolment No: 92600565002 ")
print("Name: Rajveer \n")
# Object of Parent Class
generic_animal = Animal()
print("Calling Animal's speak method:")
generic_animal.speak()
print()
# Object of Child Class
dog = Dog()
print("Calling Dog's overridden speak method:")
dog.speak()
