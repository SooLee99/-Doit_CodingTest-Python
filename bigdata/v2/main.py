def get_summary(filename):
    num_questions = 0
    num_students = 0
    total_score = 0
    best_score = 0

    file = open(filename, "r")

    # file.readlines() : 각 줄을 element 로 하는 리스트를 반환.
    lines = file.readlines()
    file.close()

    # 2D answer list of students
    answers = []

    # Preprocessing input data
    for line in lines:
        answers.append([])  # [[]]
        for i in line.lower().split(','):
            answers[-1].append(i.strip())

    # using list compreshension
    # for line in lines:
    #     answers.append([i.strip() for i in line.lower().split(',')])

    # Pop the correct answers
    c_answers = answers.pop(0)

    num_questions = len(c_answers)
    num_students = len(answers)

    # score list of students
    s_scores = []

    # using index-based for loop
    for i in range(num_students):
        s_scores.append(0)
        for j in range(num_questions):
            if answers[i][j] == c_answers[j]:
                s_scores[-1] += 4

    # using zip
    # for s_answers in answers:
    #     s_scores.append(0)
    #     for s, c in zip(s_answers, c_answers):
    #         if s == c:
    #             s_scores[-1] += 4

    total_score = sum(s_scores)
    best_score = max(s_scores)

    return (num_questions,
            num_students,
            total_score,
            best_score)


num_q, num_s, total, best = get_summary("data/answers.csv")

print(f"# of questions: {num_q}")
print(f"# of students: {num_s}")
print(f"total score: {total}")
print(f"avg. score: {(total / num_s) if num_s != 0 else 0:.2f}")
print(f"best score: {best}")