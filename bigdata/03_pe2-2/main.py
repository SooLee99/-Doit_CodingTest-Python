# 문제 : 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
#       s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
#       'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# (1) for문을 사용하는 방법
def solution(s):
    p_count = 0
    y_count = 0
    low_s = s.lower()

    for c in low_s:
        if c == 'p':
            p_count += 1

        elif c == 'y':
            y_count += 1

        return p_count == y_count

# (2) count()를 사용하는 방법
def solution(s):
    low_s = s.lower()
    return low_s.count('p') == low_s.count('y')

# 출력 결과
print(solution("pPoooyY"))
print(solution("Pyy"))