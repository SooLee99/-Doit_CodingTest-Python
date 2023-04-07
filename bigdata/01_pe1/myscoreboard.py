# 파일을 읽고, 정답과 학생 답변을 분리.
def get_score_board(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # 학생들의 2차원 리스트 답변 목록
    answers = []

    # 입력 데이터 전처리
    for line in lines:
        answers.append([i.strip() for i in line.lower().split(',')])

    # 문제의 정답만 따로 분리.
    c_answers = answers.pop(0)

    # 2차원 리스트에 나머지 학생 답변을 저장
    score_board = []

    # 루프에 인덱스 기반 사용 (학생 답변에 정답을 체크한다.)
    for i in range(len(answers)):
        # 학생의 리스트(세로) 생성.
        score_board.append([])

        # 답변의 정답을 체크하고, 리스트(가로) 작성.
        for j in range(len(c_answers)):
            if answers[i][j] == c_answers[j]:
                score_board[i].append(1)
            else:
                score_board[i].append(0)

    return score_board
