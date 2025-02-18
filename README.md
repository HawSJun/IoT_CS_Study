# IoT_Study
2025 IoT 공부 리포지토리

## 개인 공부

### 변수(variable)
- 변할 수 있는 자료
- 프로그래밍 언어에서 `=` 는 변수에 값을 할당한다는 의미

### 사용자 입력
- input()
    - input 함수는 무엇을 입력해도 결과는 무조건 **문자열 자료형**
    - input 함수 괄호 안에 입력한 내용을 **프롬프트 문자열** 
    - 프로그램이 실행 도중 잠시 멈추는 것을 **블록(block)**
    - input과 같이 함수의 결과로 나오는 값을 **리턴값**
    - 입력받은 문자열을 변환 : **캐스트(cast)**

### 문자열 format() 함수
- 문자열을 가지고 있는 함수
-  `print(f'{ }')`

### 클래스(class)
- 객체를 생성하기 위한 설계도. 속성(데이터)와 메서드(기능)을 정의한다.
- 클래스의 주요 특징
    - 속성(Attributes) : 객체의 특성을 나타내는 변수
    - 메서드(Methods) : 클래스 내에서 정의된 함수
- `__init__`
    - 객체가 생성될 때 자동으로 호출되는 **초기화** 메서드
    - 클래스 생성자 메서드
    - 객체마다 **다른 초기값**을 설정할 수 있다.
    - 클래스 내부에서 데이터를 관리하기 위해 속성을 정의하고 초기화할 수 있다.
    - 객체 생성 시 불필요한 추가 작업을 중단하고, **자동화된 초기 설정**을 제공한다.

### 객체(object)
- 클래스에서 생성된 실체. 클래스의 인스턴스라고도 한다.