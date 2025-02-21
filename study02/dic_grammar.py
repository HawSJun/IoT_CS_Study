# 딕셔너리 사용

# 딕셔너러_이름[key] = value로 추가 가능
dic = {1 : 'a'}

dic[2] = 'b'
dic['apple'] = 10

print(dic)   # {1: 'a', 2: 'b', 'apple': 10}

dic[1] = 'aa'
print(dic)   # 이미 존재하는 key라면 value 값을 바꿈
             # {1: 'aa', 2: 'b', 'apple': 10}


# del 딕셔너리_이름[key]으로 삭제
del dic[1]

print(dic)  # {2: 'b', 'apple': 10}

# 딕셔너리에서 key를 사용해 value 값 얻기

a = {'Emily' : 88, 'James' : 82}

print(a['Emily'])  # 88

# 딕셔너리에는 key가 중복으로 존재할 수 없음
# 딕셔너리 key에는 변하는 값 사용 불가 -> key에 리스트는 사용불가, 튜블은 사용가능
b = {1 : 'a', 1 : 'b'}
print(b)  # {1: 'b'} 앞의 {1: 'a'}는 없어짐

# c = {[1, 2, 3]: 'baby'}
# print(c)   # unhashable type: 'list' 에러 발생

d = {(1, 2, 3): 'baby'}
print(d)  # {(1, 2, 3): 'baby'} 출력

# 리스트 관련 함수 : keys()
e = {1: 'dad', 2: 'mom', 3: 'me'}
print(e.keys())   # dict_keys([1, 2, 3]) 이렇게 출력값 나옴

print(list(e.keys()))  # [1, 2, 3] 출력

# for k in e.keys():
#     print(k)

print(e.keys())
print(e.values())
print(e.items())

print(list(e.keys()))
print(list(e.values()))
print(list(e.items()))  # 튜플로 묶은 값을 출력

print(e.clear()) # 모두 지우기 None이 나옴

# key로 value 얻기 : 두 가지 방법
# 딕셔너리이름.get() : 존재하지 않는 키로 값을 가져오려고 할 때, None을 리턴
# 딕셔너리[키] : 존재하지 않는 키로 값을 가져오려고 할 때, 오류 발생
# get(찾는 key값, 디폴트 값) : 딕셔너리 내 찾는 key가 없는 경우 미리 정해 준 디폴트 값을 반환

g = {1: 'apple', 2: 'banana', 3: 'melon'}

print(g[1])         # apple
print(g.get(1))     # apple

# print(g[4])         # 에러 발생
print(g.get(4))       # None

print(g.get(1, 'orange'))   # apple
print(g.get(4, 'cherry'))   # 딕셔너리에 없어도 디폴드 값 반환

# 해당 key가 딕셔너리 안에 있는지 조사 : in (True/False)
m = {1: 'tea', 2: 'coffee', 3: 'ade'}

print(3 in m)       # True
print(4 in m)       # False