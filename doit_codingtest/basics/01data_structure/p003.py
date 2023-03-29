# 003 문제 : 수 N개가 주어졌을 때, i번째 수에서 j번쨰 수까지의 합을 구하는 프로그램을 작성하시오.

## <입력>
# 1번째 줄에 수의 개수 N(1 <= N <= 100,000), 합을 구해야 하는 횟수 M(1 <= M <= 100,000)
# 2번째 줄에 N개의 수가 주어진다. 각 수는 1,000보다 작거나 같은 자연수다.
# 3번째 줄부터는 M개의 줄에 합을 구해야 하는 구간 i와 j가 주어진다.

## <출력>
# 1번째 줄에 새로운 평균을 출력한다. 실제제 정답과 출력 값의 절대 오차 또는 상대 오차가 10 -2승 이하이면 정답이다.

import sys
input = sys.stdin.readline
# 보통 input()으로 문자열 값을 입력 받지만 반복문으로 여러 줄을 입력 받아야 할 때는 시간 초과 문제가 발생할 수 있다고 한다.
# 따라서 이럴 경우에는 import sys로 모듈을 불러오고,
# sys.stdin.readline()을 사용하는 것이 좋다.

## 1번째 줄 입력 (N과 M)
suNo, quizNo = map(int, input().split())

## 2번째 줄 입력 (합을 구할 대상 배열)
numbers = list(map(int, input().split()))

## 합배열 구하기
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

## 출력 수행.
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])