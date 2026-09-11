class Student:
    def __init__(self,name, age,grade):
        self.name = name 
        self.age = age
        self.grade = grade

#creating objects
student1 = Student('Raj', 100, 'A+')
student2 = Student('Naj',100, 'B+')

print(student1.name, student1.age, student1.grade)
print(student2.name, student2.age, student2.grade)        
    
    
""" Constructor type-
    - default constructor
    - parametrized constructor (self,name,age)
    - constructor with default values (self, name "unknown), age = 18
"""