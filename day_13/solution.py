import time
from colorama import Fore, Back, Style
import itertools


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    lines = input.split("\n")
    games = []
    game = []
    for line in lines:
        if line == "":
            games.append(game)
            game = []
        else:
            game.append([char for char in line])

    mirror_rows = []
    mirror_columns = []
    for game in games:
        result = find_mirror(game)
        if result is not None:
            mirror_rows.append(result)
            continue
        # swap columns and rows
        game = list(map(list, zip(*game)))
        result = find_mirror(game)
        if result is not None:
            mirror_columns.append(result)
            continue
    print(mirror_columns, mirror_rows)
    total = sum(mirror_columns) + sum([100 * x for x in mirror_rows])
    return total


def solve_second(input: str):
    lines = input.split("\n")
    games = []
    game = []
    for line in lines:
        if line == "":
            games.append(game)
            game = []
        else:
            game.append([char for char in line])

    mirror_rows = []
    mirror_columns = []
    for game in games:
        found_a_repeat = False
        for i, row in enumerate(game):
            if found_a_repeat:
                break
            for k in range(len(row)):
                if row[k] == ".":
                    row[k] = "#"
                else:
                    row[k] = "."
                game[i] = row
                result = find_mirror(game)
                # check if result is not none and if row i is included in the result
                if result is not None and i > result - (len(game) - result):
                    found_a_repeat = True
                    mirror_rows.append(result)
                    break
                # swap columns and rows
                game = list(map(list, zip(*game)))
                result = find_mirror(game)
                if result is not None and k > result - (len(game) - result):
                    found_a_repeat = True
                    mirror_columns.append(result)
                    continue
                game = list(map(list, zip(*game)))
                if row[k] == ".":
                    row[k] = "#"
                else:
                    row[k] = "."
                game[i] = row
    print('columns:', mirror_columns, 'rows:', mirror_rows)
    total = sum(mirror_columns) + sum([100 * x for x in mirror_rows])
    return total


def find_mirror(game):
    for i, row in enumerate(game):
        found_a_repeat = False
        for j in range(i):
            if i - j - 1 < 0:
                break
            if i + j >= len(game):
                break
            if game[i - j - 1] == game[i + j]:
                found_a_repeat = True
            if game[i - j - 1] != game[i + j]:
                found_a_repeat = False
                break
        if found_a_repeat:
            return i


# > 22329