class MyClass:
    def my_method(self):
        print("This is a method.")

# 클래스의 인스턴스 생성
obj = MyClass()

# 메서드 호출
obj.my_method()


class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

# 정적 메서드 호출
result = Calculator.add(3, 5)
print("정적 메서드 호출 결과:", result)



class Calculator:
    def add(self, x, y):
        return x + y

# 클래스의 인스턴스 생성
calc = Calculator()

# 동적 메서드 호출
result = calc.add(3, 5)
print("동적 메서드 호출 결과:", result)
