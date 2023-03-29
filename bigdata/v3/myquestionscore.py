print(__name__)

def get_question_scores(score_board):
    results = []
    for i in range(len(score_board[0])):
        results.append(0)
        for j in range(len(score_board)):
            results[i] += score_board[j][i] # results[-1] is ok?
    return results
