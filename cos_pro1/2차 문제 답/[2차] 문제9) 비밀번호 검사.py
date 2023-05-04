"""
< 문제 >
    [2차] 문제9) 비밀번호 검사

< 문제 설명 >
    주어진 비밀번호가 안전한지 아닌지 판단하려합니다. 비밀번호의 안전 여부는 다음 규칙으로 판단합니다.
    연속된 3자리 이상의 알파벳 혹은 숫자를 사용할 수 없습니다. (abc, cba, 012, 987 등)
    비밀번호에 사용할 문자열 password가 매개변수로 주어질 때,
    주어진 문자열이 위 규칙에 맞으면 true를, 맞지 않으면 false를 return 하도록 solution 함수를 작성했습니다.
    그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
    주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

< 매개변수 설명 >
    비밀번호에 사용할 문자열 password가 solution 함수의 매개변수로 주어집니다.
    password는 알파벳 소문자와 숫자로만 이루어진 문자열입니다.
    password의 길이는 5 이상 20 이하입니다.

< return 값 설명 >
    주어진 문자열이 주어진 규칙에 맞으면 true를, 맞지 않으면 false를 return 해주세요.
"""

def solution(password):
	length = len(password)

    # second_check 부분에서 +2 => 인덱스 범위 넘지 않아야함
	for i in range(length - 2):

        # 아스키코드를 이용하여 전달받은 문자열, 숫자가 연속되지 않았는지 검사 (0번째, 1번째 자리 검사)
		first_check = ord(password[i + 1]) - ord(password[i])

        # 아스키코드를 이용하여 전달받은 문자열, 숫자가 연속되지 않았는지 검사 (1번째, 2번째 자리 검사)
		second_check = ord(password[i+2]) - ord(password[i+1])

        # 만약 first_check, second_check이 모두 걸리면서
		if first_check == second_check and (first_check == 1 or first_check == -1):
            # 1, -1인 경우 패스워드 설정에 실패하였다고 반환
			return False

	return True

password1 = "cospro890"
ret1 = solution(password1)
print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "cba323"
ret2 = solution(password2)
print("solution 함수의 반환 값은", ret2, "입니다.")
