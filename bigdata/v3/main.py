print(__name__)

from myscoreboard import get_score_board
from myquestionscore import get_question_scores
from myprint import print_question_scores
from myprint import print_score_board


def print_hello_world():
    print('hello world!')

if __name__ == '__main__':
    s_board = get_score_board("data/answers.csv")
    q_scores = get_question_scores(s_board)

    print_score_board(s_board)
    print_question_scores(q_scores)

# go to def
# ctrl + left mouse click
# or, ctrl + F12

# back
# alt + left arrow

