# print_score_board() : 문제수, 학생수, 총합계점수, 최고점수를 출력하는 함수.
def print_score_board(s_board):
    if s_board:
        print(f"# of questions: {len(s_board[0])}")
        print(f"# of students: {len(s_board)}")
        print(f"total score: {sum([sum(s) for s in s_board]) * 4}")
        print(f"best score: {max([sum(s) for s in s_board]) * 4}")


# print_question_scores() : 문제 별로 학생들의 정답 수를 리턴하는 함수.
def print_question_scores(q_scores):
    for i, score in enumerate(q_scores):
        print(f"Q.{i:02d} : {score}")