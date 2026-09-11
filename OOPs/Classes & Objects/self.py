"""Self keyword

- it refer to the specific object calling  the method
- always use self to store properties inside the object
- python automaticall pass object as a self
- without self data can't store in object
"""
"""example"""

"""class Student:
    def set_details(name, age):
        name = name
        age = age
        
Student1 = Student()
Student1.set_details("Udit", 65)
print(Student1.name)"""

"""using self"""
class Student:
    def set_details(self, name, age):
       self.name = name
       self.age = age
        
Student1 = Student()
Student1.set_details("Udit", 65)
print(Student1.name, Student1.age)

