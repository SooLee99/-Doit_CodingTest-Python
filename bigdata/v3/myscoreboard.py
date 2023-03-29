print(__name__)

def get_score_board(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    # 2D answer list of students
    answers = []

    # Preprocessing input data
    for line in lines:
        answers.append([i.strip() for i in line.lower().split(',')])

    # Pop the correct answers
    c_answers = answers.pop(0)

    # 2D score list of students
    score_board = []

    # using index-based for loop
    for i in range(len(answers)):
        score_board.append([])
        for j in range(len(c_answers)):
            if answers[i][j] == c_answers[j]:
                score_board[i].append(1)
            else:
                score_board[i].append(0)

    return score_board
