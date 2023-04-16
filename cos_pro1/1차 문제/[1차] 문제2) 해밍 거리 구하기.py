"""
< 문제 >
    해밍 거리 구하기

< 문제 설명 >
    해밍 거리(Hamming distance)란 같은 길이를 가진 두 개의 문자열에서 같은 위치에 있지만 서로 다른 문자의 개수를 뜻합니다.
    예를 들어 두 2진수 문자열이 "10010"과 "110"이라면,
    먼저 두 문자열의 자릿수를 맞추기 위해 "110"의 앞에 0 두개를 채워 "00110"으로 만들어 줍니다.
    두 2진수 문자열은 첫 번째와 세 번째 문자가 서로 다르므로 해밍 거리는 2입니다.

        `1`0`0`1 0
        `0`0`1`1 0

    두 2진수 문자열 binaryA, binaryB의 해밍 거리를 구하려 합니다. 이를 위해 다음과 같이 간단히 프로그램 구조를 작성했습니다.

    1단계. 길이가 더 긴 2진수 문자열의 길이를 구합니다.
    2단계. 첫 번째 2진수 문자열의 길이가 더 짧다면 문자열의 앞에 0을 채워넣어 길이를 맞춰줍니다.
    3단계. 두 번째 2진수 문자열의 길이가 더 짧다면 문자열의 앞에 0을 채워넣어 길이를 맞춰줍니다.
    4단계. 길이가 같은 두 2진수 문자열의 해밍 거리를 구합니다.

    두 2진수 문자열 binaryA와 binaryB가 매개변수로 주어질 때,
    두 2진수의 해밍 거리를 return 하도록 solution 함수를 작성했습니다.
    이때, 위 구조를 참고하여 중복되는 부분은 func_a라는 함수로 작성했습니다.
    코드가 올바르게 동작할 수 있도록 빈칸을 알맞게 채워 전체 코드를 완성해주세요.

< 매개변수 설명 >
    두 2진수 문자열 binaryA와 binaryB가 solution 함수의 매개변수로 주어집니다.
    binaryA의 길이는 1 이상 10 이하입니다.
    binaryA는 0 또는 1로만 이루어진 문자열이며, 0으로 시작하지 않습니다.
    binaryB의 길이는 1 이상 10 이하입니다.
    binaryB는 0 또는 1로만 이루어진 문자열이며, 0으로 시작하지 않습니다.

< return 값 설명 >
    두 2진수 문자열의 해밍 거리를 return 해주세요.
"""

# func_a() : 0을 앞에 채워 길이를 맞추는 작업을 한다.
def func_a(string, length):
	padZero = ""
	padSize = length - len(string)              # 입력된 내용 1
    # print('padSize = ', padSize)              # 입력된 내용 2 <= print()를 통해서 현재 문제의 출력 값을 확인.

	# max_length - 문자열 길이 => padSize
	# padSize란 다른 2진수 문자열의 크기보다 모자른 양
	for i in range(padSize):
		padZero += "0"
		# padSize 만큼 0을 추가
	return padZero + string
	# 추가한 0을 string 앞에 붙여 반환

def solution(binaryA, binaryB):
	# 매개 변수로 binaryA와 binaryB를 전달 받음
	max_length = max(len(binaryA), len(binaryB))

	# binaryA와 binaryB 중 더 큰 값을 max_length로 저장
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

	hamming_distance = 0
	for i in range(max_length):
		# 모든 이진수의 인덱스를 순회
		if binaryA[i] != binaryB[i]:			# 입력된 내용 3
		# 만약 두 이진수의 값이 다른 경우
			hamming_distance += 1
			# 해밍 거리 값 추가
	return hamming_distance
	# 해밍 거리 반환

binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)
print("solution 함수의 반환 값은", ret, "입니다.")