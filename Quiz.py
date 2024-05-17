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
