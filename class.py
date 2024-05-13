class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# 클래스의 인스턴스 생성
person1 = Person("Alice", 30)

# 메서드 호출
person1.display_info()
