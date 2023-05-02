"""
< 문제 >
    병합 and 정렬

< 문제 내용 >
    오름차순으로 정렬되어있는 두 리스트 arrA, arrB를 하나의 리스트로 합치려 합니다.
    단, 합친 후의 리스트도 오름차순으로 정렬되어 있어야 합니다.

    예를 들어 arrA = [-2, 3, 5, 9], arrB = [0, 1, 5]인 경우
    두 리스트을 오름차순으로 정렬된 하나의 리스트로 합치면 [-2, 0, 1, 3, 5, 5, 9]가 됩니다.

    오름차순으로 정렬된 두 리스트 arrA와 arrB가 주어졌을 때,
    두 리스트를 오름차순으로 정렬된 하나의 리스트로 합쳐서 return 하도록 solution 함수를 작성하려 합니다.
    빈칸을 채워 전체 코드를 완성해주세요.

< 매개 변수 설명 >
    오름차순으로 정렬된 두 리스트 arrA와 arrB가 solution 함수의 매개변수로 주어집니다.
    - arrA의 길이는 1 이상 200,000 이하입니다.
    - arrA의 원소는 -1,000,000 이상 1,000,000 이하의 정수입니다.
    - arrB의 길이는 1 이상 200,000 이하입니다.
    - arrB의 원소는 -1,000,000 이상 1,000,000 이하의 정수입니다.

< return 값 설명 >
    두 리스트 arrA, arrB를 오름차순으로 정렬된 하나의 리스트로 합쳐서 return 해주세요.
"""

def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA)
    arrB_len = len(arrB)
    answer = []

    # 1. arrA 및 arrB 중 한 배열의 크기만큼 순회
    while arrA_idx < arrA_len and arrB_idx < arrB_len:
        if arrA[arrA_idx] < arrB[arrB_idx]:             # 각 요소를 비교한 뒤 arrA가 더 작은 경우
            answer.append(arrA[arrA_idx])               # arrA 값을 answer에 추가
            arrA_idx += 1                               # 해당 요소는 answer에 추가하였으니 다음 요소 비교를 위해 idx 값 증가

        else:
            answer.append(arrB[arrB_idx])  # arrB 값을 answer에 추가
            arrB_idx += 1  # 해당 요소는 answer에 추가하였으니 다음 요소 비교를 위해 idx 값 증가


    # 2. 위에서 비교 후 남은 arrA 요소들을 반복
    while arrA_idx < arrA_len:
        answer.append(arrA[arrA_idx])  # answer에 arrA의 요소 추가
        arrA_idx += 1  # 다음 arrA의 요소를 추가하기 위해 idx 값 증가


    # 3. 위에서 비교 후 남은 arrB 요소들을 반복
    while arrB_idx < arrB_len:
        answer.append(arrB[arrB_idx])  # answer에 arrB의 요소 추가
        arrB_idx += 1  # 다음 arrB의 요소를 추가하기 위해 idx 값 증가

    return answer


arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);
print("solution 함수의 반환 값은", ret, "입니다.")