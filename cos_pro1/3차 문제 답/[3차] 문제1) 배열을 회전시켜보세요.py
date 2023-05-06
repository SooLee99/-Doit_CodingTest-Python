"""
< 문제 >
    [3차] 문제1) 배열을 회전시켜보세요

< 문제 설명 >
    정수로 이루어진 두 배열 arrA와 arrB가 주어질 때, arrA를 회전해 arrB로 만들 수 있는지 알아보려 합니다.
    배열의 회전이란 모든 원소를 오른쪽으로 한 칸씩 이동시키고, 마지막 원소는 배열의 맨 앞에 넣는 것을 말합니다.

    이를 위해 다음과 같이 프로그램 구조를 작성했습니다.
        1. arrA와 arrB의 길이가 다르면 false를 return 합니다.
        2. 두 배열의 구성 성분이 달라 회전했을 때 같아질 가능성이 없다면 false를 return 합니다.
        3. arrA 배열을 두 번 이어 붙여 길이가 2배인 배열로 만듭니다.
        4. arrA의 부분 배열 중 arrB와 같은 배열이 있으면 true를, 그렇지 않으면 false를 return 합니다.

    배열 arrA와 arrA의 길이 arrA_len, 배열 arrB와 arrB의 길이 arrB_len이 매개변수로 주어질 때,
    arrA를 회전해 arrB로 만들 수 있으면 true를, 그렇지 않으면 false를 return 하도록 ㅉsolution 함수를 작성하려 합니다.
    위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

< 매개변수 설명 >
    배열 arrA와 arrA의 길이 arrA_len, 배열 arrB와 arrB의 길이 arrB_len이 solution 함수의 매개변수로 주어집니다.
    - arrA_len은 1,000 이하인 자연수입니다.
    - arrA의 원소는 0 이상 1,000 이하인 정수입니다.
    - arrB_len은 1,000 이하인 자연수입니다.
    - arrB의 원소는 0 이상 1,000 이하인 정수입니다.

< return 값 설명 >
    - arrA를 회전해 arrB로 만들 수 있으면 true를, 그렇지 않으면 false를 return 해주세요.
"""

def func_a(arr):
	ret = arr + arr # 리스트를 2배로 불림
	return ret      # 2배로 불린 리스트 반환

def func_b(first, second):
	MAX_NUMBER = 1001
	counter = [0 for _ in range(MAX_NUMBER)] # 0 ~ 1001 리스트 생성

    # counter에 first second 값 누적
	for f, s in zip(first, second):
		counter[f] += 1
		counter[s] -= 1

    # counter 리스트 순회
	for c in counter:
        # counter의 리스트들이 0 이라는 것은 [f] [s]가 동일하게 arrA와 arrB에 존재한다는 것
		if c != 0:
			return False # 만약 하나라도 0이 아니라면 겹치지 않는 부분이 있다는 뜻으로 False 반환

	return True # 다 0인 경우 모든 요소의 구성 성분이 같다는 것으로 True 반환

def func_c(first, second):
	length = len(second) # arrB의 리스트의 길이를 저장

    # arrB 리스트 길이만큼 반복
	for i in range(length):
        # 만약 arrA의 부분 리스트 중 arrB와 동일한 부분이 있다면
		if first[i : i + length] == second:
			return True # True 반환

	return False        # 아닌 경우 False 반환

def solution(arrA, arrB):
    # 1. 길이가 다른 경우
	if len(arrA) != len(arrB):
		return False    # False 반환

    # 2. 두 배열의 구성 성분이 같은 경우
	if func_b(arrA,arrB):
        # 3. arrA 배열을 2배로 이어 붙임
		arrA_temp = func_a(arrA)

        # 4. 2배로 늘린 arrA 안에 arrB가 부분 배열로 있는 경우
		if func_c(arrA_temp, arrB):
			return True # 배열을 회전 시킬 경우 똑같아질 수 있기 때문에 True 반환

	return False        # 배열을 회전 시켜도 똑같아질 수 없기 때문에 False 반환


arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)
print("solution 함수의 반환 값은", ret2, "입니다.")