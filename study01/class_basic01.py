

# 클래스란 ?

# 어떤 객체의 특성,특징 등등등을 모아둔 '틀' 으로서 인스턴스를 찍어낼 수 있다.


# 기초문법

# class people():

#     # 클래스가 가지고 있는 명사 , 멤버 변수 선언 예시
#     # 멤버 변수  
#     # private : 클래스 내에서만 접근이 가능한 변수. 변수 이름 앞에 __을 붙혀주면 된다.
#     # public : 클래스 밖에서도, people.name 등으로 접근이 가능하다.

#     # __init__ (생성자) : 클래스의 인스턴스가 생성될 때 자동으로 실행되는 함수이다.

#     def __init__(self, name, hand, foot, eyes, body, face): # 매개변수 설정, 내가 input을 받아서 사용하고싶은 변수가 있다면, 매개변수를 self 이외에 설정을 해주어야한다. 여기서는 name을 선언하여 사용했다.
#         print('생성자가 실행되었습니다!')
#         self.name = name
#         self.hand = hand
#         self.foot = foot    
#         self.eyes = eyes
#         self.body = body
#         self.face = face

#     # 클래스가 할 수 있는 행동(동사), 멤버 함수(메서드) 선언 예시
#     def shake(self): # 매개변수 설정, 이 또한 아무것도 받지 않으려면 self만 설정해놓으면 된다.
#         return f'{self.name}이가 {self.hand}를 흔듭니다 !'
    

# # 클래스 사용하기

# # people 클래스의 인스턴스 생성 후 human 이라는 변수에 담았다 !
# human = people('황석준', '손', '발', '눈', '몸', '얼굴') # 생성자가 실행되었습니다!

# human.shake() # 최보정이가 발을 흔듭니다 !

# print(f'{human.name}이 {human.hand}을 흔듭니다!')


"""
- 연습 -
자신의 이름을 가진 people 인스턴스를 생성한 후 손을 흔들어보세요.

출력 결과 
생성자가 실행되었습니다!
본인의이름이가 손을 흔듭니다 !

아래에 코드 입력
"""

# class people:
#     def __init__(self, name, hand, foot, eyes, body, face):
#         print('생성자가 실행되었습니다!')
#         self.name = name
#         self.hand = hand
#         self.foot = foot    
#         self.eyes = eyes
#         self.body = body
#         self.face = face

#     def shake(self):
#         return f'{self.name}이가 {self.hand}를 흔듭니다 !'
    

# human = people('황석준', '손', '발', '눈', '몸', '얼굴') 

# human.shake()

# print(f'{human.name}이 {human.hand}을 흔듭니다!')


class People:   # People 이라는 클래스를 정의

    def __init__(self, name, hand, foot, eyes, body, face): # 클래스의 생성자. 클래스의 객체가 생성될 때 호출
        print('생성자가 실행되었습니다!')                   # name, hand, foot, eyes, body, face 매개변수를 받아 초기화
        self.name = name    # name의 인자를 받아서 객체의 name 속성에 저장
        self.hand = hand
        self.foot = foot    
        self.eyes = eyes
        self.body = body
        self.face = face

    def shake(self):        # shake라는 멤버함수(메서드)를 정의
        return f'{self.name}(가)이 {self.hand}를 흔듭니다!'     # shake 메서드가 호출되면
                                                                # 객체의 이름과 손을 흔드는 동작을 문자열로 반환

human = People('황석준', '손', '발', '눈', '몸', '얼굴')       # People 클래스의 객체(human)를 생성
                                                               # name, hand, foot, eyes, body, face 인자를 
                                                               # 각각 '황석준', '손', '발', '눈', '몸', '얼굴' 로 설정
print(human.shake()) # human.shake 메서드를 호출하여 동작을 실행

class People:
    
    def __init__(self, name, hand, foot, eyes, body, face):
        print('생성자가 실행되었습니다!')
        self.name = name
        self.hand = hand
        self.foot = foot    
        self.eyes = eyes
        self.body = body
        self.face = face

    def __str__(self):
        return f'{self.name}(가)이 {self.hand}를 흔듭니다!'
    # __str__ 메서드를 추가하면, 객체를 출력할 때 객체의 속성이나 원하는 형태로 사용자 정의 문자열을 출력할 수 있다.
    # print(human) 같은 구문을 실행하면, human 객체는 자동으로 __str__() 메서드를 호출하여 반환된 값을 출력합니다.
human = People('황석준', '손', '발', '눈', '몸', '얼굴')
print(human)