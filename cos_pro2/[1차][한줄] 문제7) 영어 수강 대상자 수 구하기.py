"""
< 문제 >
    [1차][한줄] 문제7) 영어 수강 대상자 수 구하기 - Python3

< 문제설명 >
    A 대학에서는 수준별 영어 강의를 제공하고 있습니다.
    초급 영어 강의는 토익시험에서 650점 이상 800점 미만의 성적을 취득한 학생만을 수강대상으로 하고 있습니다.
    초급 영어 강의에 수강신청한 사람이 10명일 때, 이 중에서 몇명이 수강 대상에해당하는지 확인하려합니다.
    수강신청자들의 토익 성적이 들어있는 배열 scores와 scores의 길이 scores_len이 매개변수로 주어질 때,
    수강 대상자들의 인원수를 return 하도록 solution 함수를 작성했습니다.
    그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다.
    주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정해주세요.

< 매개변수 설명 >
    수강신청자들의 토익 성적이 들어있는 배열 scores와 scores의 길이 scoreslen이 solution 함수의 매개변수로 주어집니다.
    scores의 원소는 500 이상 990 이하의 정수입니다.
    scoreslen은 10입니다.

< return 값 설명 >
    수강 대상자들의 인원수를 return 해주세요.
"""
def solution(scores):
    count = 0
    for s in scores:
    	# 토익성적이 650점 이상 800점 미만일 경우 강의 수강 대상
        if 650 <= s < 800:
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print("solution 함수의 반환 값은", ret, "입니다.")
