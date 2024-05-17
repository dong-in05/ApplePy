# 1. 기본 클래스와 객체 생성

class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()

# 2. 생성자 사용하기

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

my_car = Car("red", "Toyota")
print(my_car.color)  # red

# 3. 메서드에 데이터 전달하기

class Calculator:
    def add(self, x, y):
        return x + y

calc = Calculator()
result = calc.add(5, 3)
print(result)  # 8

# 4. 인스턴스 변수와 클래스 변수

class Student:
    school_name = "High School"  # 클래스 변수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수

student1 = Student("John")
print(student1.name)  # John
print(Student.school_name)  # High School

# 5. 상속

class Animal:
    def speak(self):
        print("I am an animal")

class Cat(Animal):
    def speak(self):
        print("Meow")

my_cat = Cat()
my_cat.speak()  # Meow

# 6. 다중 상속

class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

my_child = Child()
my_child.skills()

# 7. 데이터 은닉과 이름 장식

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Added:", amount)

account = Account("John")
account.deposit(100)

# 8. 클래스 메서드와 스태틱 메서드

class Temperature:
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5.0/9.0

    @classmethod
    def boiling_point(cls):
        return cls.fahrenheit_to_celsius(212)

print(Temperature.boiling_point())  # 100.0

# 9. 특수 메서드 사용하기 (str, len)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return 300

book = Book("Python 101", "Mike Driscoll")
print(book)  # Python 101 by Mike Driscoll
print(len(book))  # 300

# 10. 속성 관리 (@property)

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@example.com"

person = Person("John", "Doe")
print(person.email)  # John.Doe@example.com
