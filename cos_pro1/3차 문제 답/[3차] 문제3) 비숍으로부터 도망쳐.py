"""
< 문제 >
    [3차] 문제3) 비숍으로부터 도망쳐 - Python

< 문제 설명 >
    체스에서 비숍(Bishop)은 아래 그림과 같이 대각선 방향으로 몇 칸이든 한 번에 이동할 수 있습니다.
    만약, 한 번에 이동 가능한 칸에 체스 말이 놓여있다면 그 체스 말을 잡을 수 있습니다.

    8 x 8 크기의 체스판 위에 여러 개의 비숍(Bishop)이 놓여있습니다.
    이때, 비숍(Bishop)들에게 한 번에 잡히지 않도록 새로운 말을 놓을 수 있는 빈칸의 개수를 구하려고 합니다.
    위 그림에서 원이 그려진 칸은 비숍에게 한 번에 잡히는 칸들이며, 따라서 체스 말을 놓을 수 있는 빈칸 개수는 50개입니다.
    8 x 8 체스판에 놓인 비숍의 위치 bishops와 bishops의 길이 bishops_len이 매개변수로 주어질 때,
    비숍에게 한 번에 잡히지 않도록 새로운 체스 말을 놓을 수 있는 빈칸 개수를 return 하도록 solution 함수를 완성해주세요.

< 매개변수 설명 >
    체스판에 놓인 비숍의 위치 bishops와 bishops의 길이인 bishops_len이 solution 함수의 매개변수로 주어집니다.
    bishops는 비숍의 위치가 문자열 형태로 들어있는 배열입니다.
    bishops_len은 64 이하인 자연수입니다.
    비숍이 놓인 위치는 알파벳 대문자와 숫자로 표기합니다.
    알파벳 대문자는 가로 방향, 숫자는 세로 방향 좌표를 나타냅니다.
    예를 들어 위 그림에서 비숍이 있는 칸은 "D5"라고 표현합니다.
    한 칸에 여러 비숍이 놓이거나, 잘못된 위치가 주어지는 경우는 없습니다.

< return 값 설명 >
    비숍에게 한 번에 잡히지 않도록 새로운 체스 말을 놓을 수 있는 빈칸의 개수를 return 해주세요.
"""

def solution(bishops):
    # 1차원 리스트를 9개 생성 => 2차원 리스트 (체스판 생성)
	a = [[0]*9 for _ in range(9)]

    # 비숍의 이동 범위 저장
	dyx = [ [-1, 1], [-1, -1], [1, 1], [1, -1] ]

    # 비숍의 포지션이 저장된 리스트를 순회
	for bishop in bishops:
		x = ord(bishop[0]) - ord('A') + 1   # ord 함수를 통해 x 좌표 값 저장
		y = int(bishop[1]) - 8              # y 포지션은 int형으로만 변환 후 저장

        # 8을 뺀 이유는 파이썬의 리스트 진행 방식이 위 -> 아래 방향이기 때문임
		a[x][y] = 1     # 현재 비숍의 위치에 1 생성

        # dyx 순회하면서 비숍이 이동할 수 있는 만큼 이동
		for dx, dy in dyx:
			nx, ny = x, y   # 실시간으로 비숍의 위치를 나타낼 변수 생성 후 초기화

			while True:
				nx += dx # dyx 안에 있는 dx 값 누적
				ny += dy # dyx 안에 있는 dy 값 누적
				if ny>8 or ny<1 or nx>8 or nx<1 : break # 비숍의 이동 범위 체크

				a[nx][ny] = 1 # 비숍이 이동 가능한 위치를 1로 채움

	answer = 0
	for x in range(1, 9):
		for y in range(1, 9):
            # 비숍이 이동 불가능한 위치당 answer 1씩 누적
			if not a[x][y]: answer += 1
	return answer


bishops1 = ["D5"]
ret1 = solution(bishops1)
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)
print("solution 함수의 반환 값은", ret2, "입니다.")