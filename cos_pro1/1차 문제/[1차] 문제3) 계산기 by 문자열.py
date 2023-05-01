"""
< 문제 >
    계산기 by 문자열

< 문제 설명 >
    문자열 형태의 식을 계산하려 합니다.
    식은 2개의 자연수와 1개의 연산자('+', '-', '*' 중 하나)로 이루어져 있습니다.
    예를 들어 주어진 식이 "123+12"라면 이를 계산한 결과는 135입니다.
    문자열로 이루어진 식을 계산하기 위해 다음과 같이 간단히 프로그램 구조를 작성했습니다.

        1단계. 주어진 식에서 연산자의 위치를 찾습니다.
        2단계. 연산자의 앞과 뒤에 있는 문자열을 각각 숫자로 변환합니다.
        3단계. 주어진 연산자에 맞게 연산을 수행합니다.

    문자열 형태의 식 expression이 매개변수로 주어질 때,
    식을 계산한 결과를 return 하도록 solution 함수를 작성하려 합니다.
    위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

< 매개변수 설명 >
    문자열 형태의 식 expression이 solution 함수의 매개변수로 주어집니다.
    expression은 연산자 1개와 숫자 2개가 결합한 형태입니다.
    연산자는 '+', '-', '*'만 사용됩니다.
    숫자는 1 이상 10,000 이하의 자연수입니다.

< return 값 설명 >
    expression을 계산한 결과를 return 해주세요.
    계산 결과는 문자열로 변환하지 않아도 됩니다.
"""


def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB


def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index


def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB


def solution(expression):
    exp_index = func_ __________
    # func_b는 기호의 index 번호를 반환하는 함수임
    first_num, second_num = func_ __________
    # 기호의 index 번호와 전체 문자열 리스트를 매개 변수로 전달해야 함
    # func_c는 exp_index를 이용하여 문자열 2개를 숫자형으로 반환해 주는 함수임
    result = func_ __________
    # func_a는 기호를 보고 그에 맞게 numA와 numB를 계산하여 반환해 주는 함수임
    # 단 expression[exp_index]로 매개 변수를 전달해야 부호를 판별할 수 있음
    return result

expression = "123+12"
ret = solution(expression)
print("solution 함수의 반환 값은", ret, "입니다.")