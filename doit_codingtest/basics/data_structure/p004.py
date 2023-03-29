# 004 문제 : 수 N개가 주어졌을 때, i번째 수에서 j번쨰 수까지의 합을 구하는 프로그램을 작성하시오.

## <입력>
# 1번째 줄에 표의 개수 N(1 <= N <= 1024)과, 합을 구해야 하는 횟수 M(1 <= M <= 100,000)
# 2번째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다.
# 다음 M개의 줄에는 4개의 정수 x1, x2, y1, y2가 주어지며, (x1, y1)에서 (x2, y2)의 합을 구해 출력해야 한다.
# 표에 채워져 잇는 수는 1,000qhek

## <출력>
# 1번째 줄에 새로운 평균을 출력한다. 실제제 정답과 출력 값의 절대 오차 또는 상대 오차가 10 -2승 이하이면 정답이다.

import sys
input = sys.stdin.readline

## 1번째 줄 입력 (n : 리스트 크기, m : 질문의 개수)
n, m = map(int, input().split())

## 리스트 제작 (A : 원본 리스트, D : 합 배열 리스트)
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

## 리스트 채우기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

## 합배열 채우기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

## 질문에 대한 답변하기
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
