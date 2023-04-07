# answers.csv 파일을 읽어 사전평가에 대한 문제 수, 학생 수, 총 합계 점수, 최고 점수를 튜플로 리턴하는 함수를 작성하시오.
# 문제당 점수는 4점 입니다.

from myscoreboard import get_score_board
from myquestionscore import get_question_scores
from myprint import print_question_scores
from myprint import print_score_board

# get_score_board() : 파일을 읽고, 정답과 학생 답변을 분리하여 정답을 체크함.
s_board = get_score_board("data/answers.csv")

# get_question_scores() : 학생 별로 정답의 개수를 세는 함수.
q_scores = get_question_scores(s_board)

# 문제수, 학생수, 총합계점수, 최고점수를 출력하는 함수.
print_score_board(s_board)

# 문제 별로 학생들의 정답 수를 리턴하는 함수.
print_question_scores(q_scores)