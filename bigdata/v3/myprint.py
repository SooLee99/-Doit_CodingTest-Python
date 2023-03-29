print(__name__)


def print_score_board(s_board):
    if s_board:
        print(f"# of questions: {len(s_board[0])}")
        print(f"# of students: {len(s_board)}")
        print(f"total score: {sum([sum(s) for s in s_board]) * 4}")
        print(f"best score: {max([sum(s) for s in s_board]) * 4}")


def print_question_scores(q_scores):
    for i, score in enumerate(q_scores):
        print(f"Q.{i:02d} : {score}")