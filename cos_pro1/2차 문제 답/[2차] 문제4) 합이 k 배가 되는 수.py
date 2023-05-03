"""
< 문제 >
    [2차] 문제4) 합이 k 배가 되는 수

< 문제 설명 >
    자연수가 중복 없이 들어있는 배열이 있습니다. 이 배열에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법은 몇 가지인지 세려고 합니다.
    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 매개변수로 주어질 때,
    이 배열에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법의 가짓수를 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    자연수가 들어있는 배열 arr와 arr의 길이 arr_len이 solution 함수의 매개변수로 주어집니다.
    arr_len은 3 이상 100 이하의 자연수입니다.
    arr에는 1 이상 1,000 이하의 자연수가 중복 없이 들어있습니다.
    K는 1 이상 10 이하의 자연수입니다.

< return 값 설명 >
    배열에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법의 가짓수를 return 해주세요.
    그러한 방법이 없다면 0을 return 하면 됩니다.
"""

def solution(arr, K):
	answer = 0

    # 배열의 0번 요소부터 마지막-2번 요소까지 반복
	for i in range(len(arr)-2):

        # 배열의 1번 요소부터 마지막-1번 요소까지 반복
		for j in range(i+1, len(arr)-1):

            # 배열의 2번 요소부터 마지막 요소까지 반복
			for k in range(j+1, len(arr)):

                # i = 0, j = 1, k = 0->1->2 식으로 모든 요소를 하나하나 비교
				if (arr[i]+arr[j]+arr[k])%K == 0 :
                    # 요소 순회 중 K로 나누었을 때의 나머지가 0(K의 배수)이면 answer 값 1씩 누적
                    answer += 1

	return answer


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)
print("solution 함수의 반환 값은", ret, "입니다.")