# N개의 수 중에서 다른 두 수의 합으로 표현 되는 수의 모든 경우의 수 구하기

def get_good_number(str_data: str):
    number_list = list(map(int, str_data.split(' ')))
    list_len = len(number_list)
    cnt = 0
    number_list.sort()

    for k in range(list_len):
        find = number_list[k]
        i = 0
        j = list_len - 1

        while i < j:
            if number_list[i] + number_list[j] < find:
                i += 1
            elif number_list[i] + number_list[j] == find:
                if i != k and j != k:
                    cnt += 1
                    break
                elif i == k:
                    i += 1
                elif j == k:
                    j -= 1
            else:
                j -= 1
    return cnt