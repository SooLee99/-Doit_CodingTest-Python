"""
< 문제 >
    [3차] 문제2) 팰린드롬 문제

< 문제 설명 >
    앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
    예를 들어, "aba"는 팰린드롬이며 "abccca"는 팰린드롬이 아닙니다.
    어떤 문자열의 부분 문자열 중 팰린드롬인 문자열이 여럿일 수 있습니다.
    이 중 k번째로 큰 팰린드롬을 알고 싶습니다. k번째로 큰 팰린드롬이란,
    모든 팰린드롬을 사전 순으로 나열했을 때 k번째에 위치하는 팰린드롬을 뜻합니다.
    이를 위해 다음과 같이 프로그램 구조를 세웠습니다.

    1. 팰린드롬 문자열을 저장할 배열 palindromes를 선언합니다.
    2. 주어진 문자열의 모든 부분 문자열을 찾아 다음을 수행합니다.
        2-1. 부분 문자열이 팰린드롬 문자열인지 확인하고, 팰린드롬 문자열이라면 palindromes에 같은 문자열이 이미 들어있는지 확인합니다.
        2-2. palindromes에 같은 문자열이 없으면, 현재 팰린드롬 문자열을 추가합니다.
    3. palindromes를 정렬합니다.
    4. 배열 길이가 k보다 작다면 "NULL"을 리턴합니다.
    5. 그렇지 않으면 배열의 k-1번째 원소를 리턴합니다.

    문자열 s와 숫자 k가 매개변수로 주어질 때, k번째로 큰 팰린드롬 문자열을 return 하도록 solution 함수를 작성하려 합니다.
    위 구조를 참고하여 코드가 올바르게 동작하도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

< 매개변수 설명 >
    문자열 s와 숫자 k가 solution 함수의 매개변수로 주어집니다.
    s의 길이는 1 이상 100 이하입니다.
    s는 알파벳 소문자로만 구성됩니다.
    k는 200 이하인 자연수입니다.

< return 값 설명 >
    k번째로 큰 팰린드롬 문자열을 return 해주세요.
    단, s로 만들 수 있는 팰린드롬 수가 k개 미만이면 "NULL"을 return 해주세요.
"""

# 팰린드롬 문자열이 palindromes 리스트에 포함되어 있는 지 확인하는 함수
def func_a(arr, s):
	return s in arr

# 팰린드롬 문자열인지 확인하는 함수
def func_b(s):
	length = len(s)
	for i in range(length // 2):
		if s[i] != s[length - i - 1]:
			return False
	return True

# palindromes 리스트를 정렬하고,
# 배열의 길이가 K보다 작은 경우 NULL을 그렇지 않은 경우 배열의 N-1를 리턴하는 함수
def func_c(palindromes, k):
	palindromes = sorted(palindromes)
	if len(palindromes) < k:
		return "NULL"
	else:
		return palindromes[k - 1]

def solution(s, k):
	palindromes = []    # 1. 팰린드롬 문자열을 저장할 리스트 선언
	length = len(s)     # 전달된 문자열의 길이를 저장

    # 저장된 길이만큼 반복
	for start_idx in range(length):
        # 부분 문자열을 커팅하기 위한 범위
		for cnt in range(1, length - start_idx + 1):
            # 문자열에서 슬라이싱을 통해 부분 문자열 저장
			sub_s = s[start_idx : start_idx + cnt]

            # 팰린드롬 문자열인지 확인 => 팰린드롬 문자열이라면
			if func_b(sub_s) == True:
                # palindromes 리스트에 포함되어 있는지 확인
				if func_a(palindromes, sub_s) == False:
                    # 부분 문자열을 palindromes 리스트에 추가
					palindromes.append(sub_s)

	answer = func_c(palindromes, k)

	# K번째로 큰 팰린드롬 문자열을 반환 => 배열의 크기보다 K가 큰 경우 NULL 반환
	return answer


s1 = "abcba"
k1 = 4
ret1 = solution(s1, k1)
print("solution 함수의 반환 값은", ret1, "입니다.")

s2 = "ccddcc"
k2 = 7
ret2 = solution(s2, k2)
print("solution 함수의 반환 값은", ret2, "입니다.")