from statistics import mean

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if(mean(self.marks)>50):
            return True
        else:
            return False

student_1 = Student("Rafal",[63,54,54])
student_2 = Student("Jakub",[1,1,1])

print(student_1.name,Student.is_passed(student_1))
print(student_2.name,Student.is_passed(student_2))