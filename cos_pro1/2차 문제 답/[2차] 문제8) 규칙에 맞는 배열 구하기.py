"""
< 문제 >
    [2차] 문제8) 규칙에 맞는 배열 구하기

< 문제 설명 >
    자연수가 들어있는 배열이 주어질 때, 다음 규칙에 따라 새로운 배열을 만들려고 합니다.
    - 주어진 배열의 첫 번째 원소를 새로운 배열의 첫 번째 원소에 넣습니다.
    - 주어진 배열의 마지막 원소를 새로운 배열의 두 번째 원소에 넣습니다.
    - 계속해서 주어진 배열의 남아있는 원소중 가장 앞에있는 원소와 가장 뒤에있는 원소를 번갈아 가져와 새로운 배열에 순서대로 넣습니다.
    - 주어진 배열에 더이상 원소가 남아있지 않을 때까지 위 과정을 반복합니다.

    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 매개변수로 주어질 때,
    위 과정을 수행해서 만든 새로운 배열을 return 하도록 solution 함수를 작성했습니다.
    그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
    주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

< 매개변수 설명 >
    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 solution 함수의 매개변수로 주어집니다.
    - arr_len은 1 이상 1,000 이하의 자연수입니다.
    - arr의 원소는 1 이상 10,000 이하의 자연수입니다.

< return 값 설명 >
    문제에 주어진 과정을 수행해서 만든 새로운 배열을 return 해주세요.
"""

def solution(arr):
	left, right = 0, len(arr) - 1
	idx = 0
	answer = [0 for _ in range(len(arr))]

    # left 값이 right 값을 넘을때까지 반복
	while left <= right:
        # 만약 idx가 짝수인 경우
		if idx % 2 == 0:
			answer[idx] = arr[left] # left 인덱스를 answer 리스트에 저장
			left += 1               # left 인덱스 증가

        # 만약 idx가 홀수인 경우
		else:
			answer[idx] = arr[right] # right 인덱스를 answer 리스트에 저장
			right -= 1              # right 인덱스 증가

        # idx 증가 시켜 answer의 다음 요소에 추가할 수 있도록 함
		idx += 1

	return answer


arr = [1, 2, 3, 4, 5, 6]
ret = solution(arr)
print("solution 함수의 반환 값은", ret, "입니다.")