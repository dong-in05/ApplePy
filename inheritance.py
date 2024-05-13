class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

# Dog 클래스의 인스턴스 생성
dog = Dog()

# 상속받은 메서드 호출
dog.speak()  # 출력: Dog barks.
