

class Student:

    counter = 1

    def __init__(self, input_name):
        self.roll = Student.counter
        self.name = input_name

        Student.counter += 1

    def __str__(self):
        return f"name :{self.name} roll num:{self.roll}"





s1 = Student('A')
print(s1)

s2 = Student('b')
print(s2)