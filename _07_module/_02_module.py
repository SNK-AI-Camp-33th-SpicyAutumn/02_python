"""
# 모듈이란?
- .py 파일을 의미
- 프로그램 내 코드 재사용성을 높이기 위해 모듈 단위로 코드를 관리
- 모듈에 작성된 변수, 함수, 클래스 등은 외부에서 import해 사용 가능
- 단, _, __ 시작하는 이름은 "내부용(private)"이라는 관례가 있음
    -> 외부에서 import 해서 사용하는 것을 지양
- import * -> 모듈 내 모든 변수, 함수, 클래스 가져오기
           -> 단, _, __로 시작하는 변수, 함수, 클랙스는 자동 제외
"""

# 파이썬 내장 모듈 math 가져오기
import math

print("math.pi: ", math.pi)

# dir(모듈명) 내장 함수: 해당 모듈의 사용 가능한 속성/함수 등을 나열
print("dir(math): ", dir(math))

# dir() 내장 함수: 현재 모듈(_02_module.py)의 사용 가능한 속성/함수 등을 나열
print("dir(): ", dir())


# 모듈명 확인(__name__)
# - import 시에는 모듈명.py -> 모듈명 반환
# - 현재 모듈 실행 시에는" __main__" 반환
print("__name__: ", __name__)
print("math.__name__: ", math.__name__)

print("-" * 50)

""" 사용자 정의 모듈 가져오기 """
# import skn.my_math

# print("skn.my_math.pi: ", skn.my_math.pi)

""" 파이썬 패키지로 모듈 가져오기 """
# skn 폴더 == 패키지
from skn import my_math  # skn 패키지 내에서 my_math 모듈 가져오기
print("my_math.pi: ", my_math.pi)
print("my_math.x: ", my_math.x)
print("my_math.get_circle_area(10): ", my_math.get_circle_area(10))
