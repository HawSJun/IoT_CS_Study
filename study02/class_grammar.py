class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()         # 객체 cal1 생성
cal2 = Calculator()         # 객체 cal2 생성

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(3))
print(cal1.add(7))
print(cal1.sub(1))

# 객체와 인스턴스 차이
# cal1 = Calculator()에서 Calculator()의 결과값을 리턴 받은 cal1가 객체
# cal1 객체는 Calculator()의 인스턴스 -> 인스턴스는 특정 객체가 어떤 클래스의 객체인지 관계위주로 설명할때 사용


class Car:
    def __init__(self, model):
        self.model = model

    def start(self):  # 이 함수는 메서드(멤버 함수)
        print(f"{self.model} is starting.")

my_car = Car("Tesla")  # my_car는 객체
my_car.start()  # my_car 객체에서 start() 메서드 호출
