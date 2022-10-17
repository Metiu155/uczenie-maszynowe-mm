class Library:
    def __init__(self, city, street, zip_code, open_hours,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
     
    def __str__(self):
        return f'Library {self.city} {self.street} {self.zip_code} {self.open_hours} {self.phone}'
    

class Employee:
    def __init__(self,first_name, last_name, hire_date, birth_date, city, street, zip_code,  phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
        
    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name} {self.hire_date} {self.birth_date} {self.city} {self.street} {self.zip_code} {self.phone}  '


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book: {self.library} {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}  '

class Order:
    def __init__(self,employee, student, books:list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
    def __str__(self):
        return f'Order: {self.employee} {self.student} {self.books} {self.order_date}  '

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Student: {self.name} {self.surname}  '

Library1 = Library('Katowice','Mariacka 5','40-232', '9-18','222-222-222')
Library2 = Library('Katowice','Stefana 7','40-482', '6-20','111-111-111')
        
Employee1 = Employee("Jan","Nowak","04-10-2021", "18-07-1997", "Katowice", "Buby 2", "40-222", "333-333-333")
Employee2 = Employee("Piotr","Kowalski","04-11-2022", "13-05-1999", "Katowice", "Huby 2", "40-111", "444-444-444")  
Employee3 = Employee("Rafal","Kik","05-12-2018", "12-03-1993", "Katowice", "Kriga 2", "40-333", "555-555-555")  

Book1 = Book(Library1,"19-12-2019","Piotr","Matuszak","69")
Book2 = Book(Library1,"19-12-2018","Piotr","Matuszak","420")
Book3 = Book(Library1,"19-12-2017","Piotr","Matuszak","6969")
Book4 = Book(Library1,"19-12-2020","Rafal","Kestowicz","42069")
Book5 = Book(Library1,"19-12-2021","Jakub","Kwiatek","69420")

student1 = Student("Rafik","Kowalski")
student2 = Student("Piter","Nowak")
student3 = Student("Kuba","Kowal")

order1 = Order(Employee1,student1,Book1,"20-04-2022")
order2 = Order(Employee2,student2,Book2,"12-02-2022")
print(order1)
print(order2)

