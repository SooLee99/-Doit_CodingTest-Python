# 문제 : 정수를 담고 있는 배열 arr의 평균 값을 return하는 함수, solution을 완성해보세요.

# (1) for문을 사용하는 방법
def solution(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum / len(arr)


# (2) sum()를 사용하는 방법
def solution(arr):
    return sum(arr) / len(arr)


# (3). numpy 라이브러리를 사용하는 방법.
import numpy
def solution(arr):
    return numpy.average(arr)


# 출력 결과
print(solution([1, 2, 3, 4]))
print(solution([5, 5]))