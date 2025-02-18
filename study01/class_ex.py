class Dog:
    # 초기회 메서드
    def __init__(self, name, age):  # 객체가 생성될 때 자동으로 호출되는 초기화 메서드
        self.name = name            # self : 생성된 객체 자신을 참조하며, 속성을 초기화하는 데 사용
        self.age = age


    # 메서드
    def bark(self):                 # bark 메서드 : 강아지가 짖는 동작을 정의한 사용자 정의 메서드
        print(f'{self.name}가 멍멍 짖습니다!')

# 객체 생성
dog1 = Dog('바둑이', 3)
dog2 = Dog('초코', 5) 

# 메서드 호출
dog1.bark()
dog2.bark()

# 속성 접근
print(f'{dog1.name}의 나이는 {dog1.age}살입니다!')
print(f'{dog2.name}의 나이는 {dog2.age}살입니다!')

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        return sum(self.data) / len(self.data)
    
    def get_max_value(self):
        return max(self.data)
    
numbers = [10, 20, 30, 40, 50]
analyzer = DataAnalyzer(numbers)

print(f'평균 값 : {analyzer.calculate_average()}')
print(f'최대 값 : {analyzer.get_max_value()}')