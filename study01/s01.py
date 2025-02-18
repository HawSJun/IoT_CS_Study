# a, b = input('숫자 두 개를 입력하세요 : ').split()
# print(a + b)  # 10 + 20 = 1020

# input에서 입력받은 값은 문자열이고, 이 문자열은 split으로 분리해도 문자열이기 떄문
# 문자열 '10 20'을 공백을 기준으로 분리하여 a에는 '10', b에는 '20'이 저장되므로
# +로 연결하면 '1020'이 나옴

# split() : 공백을 기준으로 분리하여 변수에 차례대로 저장
# map을 사용해서 정수로 변환
# map(int, input('숫자 두 개를 입력하세요 : ').split())

# a, b, c = input('숫자 입력 : ').split()

# a = int(a)
# b = int(b)
# c = int(c)

# print(a + b + c)

a, b, c = map(int, input('숫자 입력 :').split())
print(a + b + c)
