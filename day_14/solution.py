import time
from colorama import Fore, Back, Style
import itertools


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    # get a matrix of the input
    board = [[char for char in line] for line in input.split("\n")]
    for row in board:
        print("".join(row))
        
    moved = True
    while moved:
        moved = move_all_north(board)
        for row in board:
            print("".join(row))
        print()
        total = calculate_score(board)
        print(total)
    return total

def move_all_north(board):
    moved = False
    for i, row in enumerate(board):
        for k in range(len(row)):
            if i == 0:
                continue
            if row[k] == "O" and board[i-1][k] == ".":
                board[i][k] = "."
                board[i-1][k] = "O"
                moved = True
    return moved

def move_all_north_completely(board):
    moved = True
    while moved:
        moved = move_all_north(board)

def move_all_south(board):
    moved = False
    for i, row in enumerate(board):
        for k in range(len(row)):
            if i == len(board) - 1:
                continue
            if row[k] == "O" and board[i+1][k] == ".":
                board[i][k] = "."
                board[i+1][k] = "O"
                moved = True
    return moved

def move_all_south_completely(board):
    moved = True
    while moved:
        moved = move_all_south(board)

def move_all_east(board):
    moved = False
    for i, row in enumerate(board):
        for k in range(len(row)):
            if k == len(row) - 1:
                continue
            if row[k] == "O" and board[i][k+1] == ".":
                board[i][k] = "."
                board[i][k+1] = "O"
                moved = True
    return moved

def move_all_east_completely(board):
    moved = True
    while moved:
        moved = move_all_east(board)

def move_all_west(board):
    moved = False
    for i, row in enumerate(board):
        for k in range(len(row)):
            if k == 0:
                continue
            if row[k] == "O" and board[i][k-1] == ".":
                board[i][k] = "."
                board[i][k-1] = "O"
                moved = True
    return moved

def move_all_west_completely(board):
    moved = True
    while moved:
        moved = move_all_west(board)

def calculate_score(board):
    total = 0
    for i, row in enumerate(board):
        for k in range(len(row)):
            if row[k] == "O":
                total += len(board) - i
    return total

def solve_second(input: str):
    board = [[char for char in line] for line in input.split("\n")]
    
    i = 1_000_000_000
    curre_time = time.time()
    board_states = set()
    cycle_length = 0
    search_for_cycle = False
    skipped = False
    while i > 0:
        scores = []
        move_all_north_completely(board)
        scores.append(calculate_score(board))
        move_all_west_completely(board)
        scores.append(calculate_score(board))
        move_all_south_completely(board)
        scores.append(calculate_score(board))
        move_all_east_completely(board)
        scores.append(calculate_score(board))
        
        i -= 1
        
        board_states.add(tuple(tuple(row) for row in board))
        if i % 200 == 0:
            print(len(board_states))
        if i % 200 == 0 and len(board_states) > 1 and search_for_cycle and not skipped:
            cycle_length = len(board_states)
            print("cycle length:", cycle_length, "i:", i)
            i = i % cycle_length
            print("skipping to:", i)
            skipped = True
        if i < 999_999_800 and not search_for_cycle:
            search_for_cycle = True
            print("searching for cycle")
            print(len(board_states))
            board_states.clear()
        if(skipped):
            print(scores)
            # for row in board:
            #     print("".join(row))
    return 0
    

# > 95985