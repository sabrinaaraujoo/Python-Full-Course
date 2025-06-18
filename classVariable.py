class Student:

    class_year = 2029
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.num_students += 1


student1 = Student("Julia", 22)
student2 = Student("Sabrina", 25)
student3 = Student("Alex", 24)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)