"""
< 문제설명 >
    자연수가 들어있는 배열이 있습니다.
    이 배열에서 가장 많이 등장하는 숫자의 개수는 가장 적게 등장하는 숫자 개수의 몇 배인지 구하려 합니다.
    이를 위해 다음과 같이 간단히 프로그램 구조를 작성했습니다.

        1단계. 배열에 들어있는 각 자연수의 개수를 셉니다.
        2단계. 가장 많이 등장하는 수의 개수를 구합니다.
        3단계. 가장 적게 등장하는 수의 개수를 구합니다.
        4단계. 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇 배 더 많은지 구합니다.

    단, 몇 배 더 많은지 구할 때는 소수 부분은 버리고 정수 부분만 구하면 됩니다.
    자연수가 들어있는 배열 arr와 arr의 길이 arrlen이 매개변수로 주어질 때,
    가장 많이 등장하는 숫자가 가장 적게 등장하는숫자보다 몇 배 더 많은지 return 하도록 solution 함수를 작성하려 합니다.
    위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 funca, funcb, funcc 함수와 매개변수를 알맞게 채워주세요.

< 매개변수 설명 >
    자연수가 들어있는 배열 arr와 arr의 길이 arrlen이 solution 함수의 매개변수로 주어집니다.
    * arrlen은 3 이상 1,000 이하의 자연수입니다. * arr에는 1 이상 1,000이하의 자연수가 들어있습니다.

< return 값 설명 >
    배열에서 가장 많이 등장하는 숫자가 가장 적게 등장하는 숫자보다 몇 배 이상 많은지 return 해주세요.
    가장 많이 들어있는 수의 개수와 가장 적게 들어있는 수의 개수가 같은 경우에는 1을 return 합니다.
"""

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def func_a(arr):
    counter = [0 for _ in range(1001)]

    for x in arr:
        counter[x] += 1
        return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):              # [ ? 안에 정답을 입력하기 ]
    counter = func_a(arr)       # counter = ???
    max_cnt = func_b(counter)   # max_cnt = ???
    min_cnt = func_c(counter)   # min_cnt = ???
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")