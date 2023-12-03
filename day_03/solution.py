import re

def get_map(input: str):
    return [list(line) for line in input.splitlines()]

def check_if_number_valid(number_map: list, i: int, j_begin: int, j_end: int):
    for j in range(j_begin, j_end + 1):
        for i_offset in range(-1, 2):
            for j_offset in range(-1, 2):
                if i_offset == 0 and j_offset == 0:
                    continue
                i_check = i + i_offset
                j_check = j + j_offset
                if i_check < 0 or j_check < 0 or i_check >= len(number_map) or j_check >= len(number_map[i_check]):
                    continue
                if number_map[i_check][j_check] != '.' and not number_map[i_check][j_check].isdigit():
                    return True
    return False

def get_gear_value(numbers: list, gear: tuple, number_map: list):
    i = gear[0]
    j = gear[1]
    adjacent_numbers = []
    for number in numbers:
        number_i = number[0]
        number_start = number[1]
        number_end = number[2]
        if number_i == i:
            if number_start == j + 1 or number_end == j - 1:
                adjacent_numbers.append(number)
        elif number_i == i + 1 or number_i == i - 1:
            for j_offset in range(-1, 2):
                if number_start == j + j_offset or number_end == j + j_offset:
                    adjacent_numbers.append(number)
                    break
    if len(adjacent_numbers) == 2:
        gear_value = 1
        for number in adjacent_numbers:
            number_i = number[0]
            number_start = number[1]
            number_end = number[2]
            number_value = int(''.join(number_map[number_i][number_start:number_end + 1]))
            gear_value *= number_value
        return gear_value
    return 0


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    number_map = get_map(input)
    numbers = []
    for i in range(len(number_map)):
        number_start = -1
        number_end = -1
        for j in range(len(number_map[i])):
            if number_map[i][j].isdigit():
                if number_start == -1:
                    number_start = j
                number_end = j
            elif number_start != -1:
                numbers.append((i, number_start, number_end))
                number_start = -1
                number_end = -1
        if number_start != -1:
            numbers.append((i, number_start, number_end))
    for number in numbers:
        i = number[0]
        number_start = number[1]
        number_end = number[2]
        number_value = int(''.join(number_map[i][number_start:number_end + 1]))
        if not check_if_number_valid(number_map, i, number_start, number_end):
            continue
        print(number_value)
        total += number_value
    return total
        
def solve_second(input: str):
    total = 0
    number_map = get_map(input)
    numbers = []
    gears = []
    for i in range(len(number_map)):
        number_start = -1
        number_end = -1
        for j in range(len(number_map[i])):
            if number_map[i][j].isdigit():
                if number_start == -1:
                    number_start = j
                number_end = j
            elif number_start != -1:
                numbers.append((i, number_start, number_end))
                number_start = -1
                number_end = -1
        if number_start != -1:
            numbers.append((i, number_start, number_end))
    for i in range(len(number_map)):
        for j in range(len(number_map[i])):
            if number_map[i][j] == '*':
                gears.append((i, j))
    for gear in gears:
        gear_value = get_gear_value(numbers, gear, number_map)
        total += gear_value
    return total