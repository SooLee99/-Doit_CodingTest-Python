# 과제 1
answers.csv 파일을 읽어 사전평가에 대한 문제수, 학생수, 총합계점수, 최고점수를 튜플로 리턴하는 함수를 작성하시오. 문제당 점수는 4점 입니다.

## 함수 템플릿
~~~
def get_summary(filename):
    num_questions = 0
    num_students = 0
    total_score = 0
    best_score = 0

    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    
    ##########################
    # your code here
    ##########################

    return (num_questions,
            num_students,
            total_score,
            best_score)
~~~

## 기대 결과값
    # of questions: 25
    # of students: 76
    total score: 3760
    best score: 92

## 제약사항
단, numpy, pandas 와 같은 외부 라이브러리를 사용하지 말고, 기본 라이브러리만을 사용하여 구현 하세요.