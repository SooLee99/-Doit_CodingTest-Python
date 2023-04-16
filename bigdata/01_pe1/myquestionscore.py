# get_question_scores() : 학생 별로 정답의 개수를 세는 함수.
def get_question_scores(score_board):
    results = []

    for i in range(len(score_board[0])):
        results.append(0)

        for j in range(len(score_board)):
            results[i] += score_board[j][i] # results[-1] is ok?

    return results