import time
from colorama import Fore, Back, Style
import itertools
from heapq import heappush, heappop


def fill_polygon_python(polygon, min_row, max_row, min_col, max_col):
    # Convert the polygon string into a set of wall positions and find min/max rows and columns
    wall_positions = polygon

    # Helper function to get adjacent points
    def get_adjacent_points(row, col):
        return [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

    # Find a starting point inside the polygon
    def find_starting_point():
        for row in range(min_row + 1, max_row):
            for col in range(min_col, max_col):
                if (row, col) in wall_positions:
                    return row, col + 1
        return None

    # Main filling function
    filled_positions = set()
    stack = [find_starting_point()]
    i = 0
    while stack:
        
        point = stack.pop()
        if point is None:
            continue

        row, col = point

        if point not in wall_positions and point not in filled_positions:
            filled_positions.add(point)
            for adjacent_point in get_adjacent_points(row, col):
                i += 1
                if i % 10000 == 0:
                    print(i, len(stack))
                if adjacent_point not in wall_positions and adjacent_point not in filled_positions:
                    stack.append(adjacent_point)
    return filled_positions

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    
    instructions = [line.split(' ') for line in input.split('\n')]
    position = (0, 0)
    positions = set()
    for instruction in instructions:
        for i in range(int(instruction[1])):
            if instruction[0] == 'U':
                position = (position[0] - 1, position[1])
            elif instruction[0] == 'D':
                position = (position[0] + 1, position[1])
            elif instruction[0] == 'L':
                position = (position[0], position[1] - 1)
            elif instruction[0] == 'R':
                position = (position[0], position[1] + 1)
            positions.add(position)
    
    min_row = min(positions, key=lambda x: x[0])[0]
    max_row = max(positions, key=lambda x: x[0])[0]
    min_col = min(positions, key=lambda x: x[1])[1]
    max_col = max(positions, key=lambda x: x[1])[1]
    # fill inside
    print_positions(positions, min_row, max_row, min_col, max_col, set())
    fill_positions = set()
    fill_positions = fill_polygon_python(positions, min_row, max_row, min_col, max_col)
    print_positions(positions, min_row, max_row, min_col, max_col, fill_positions)
    
    total = len(fill_positions) + len(positions)
    return total

def print_positions(positions, min_row, max_row, min_col, max_col, fill_positions):
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if (row, col) in positions:
                print(Fore.GREEN + '#' + Fore.RESET, end='')
            elif (row, col) in fill_positions:
                print(Fore.YELLOW + '#' + Fore.RESET, end='')
            else:
                print('.', end='')
                continue
        print(row)

def get_instruction(input: str):
    direction = input[-2:-1]
    if direction == '0':
        direction = 'R'
    if direction == '1':
        direction = 'D'
    if direction == '2':
        direction = 'L'
    if direction == '3':
        direction = 'U'
    quantity = input[0:-2]
    # hex to int
    quantity = int(quantity, 16)
    return (direction, quantity)

def solve_second(input: str):
    total = 0
    
    instructions = [get_instruction(line.split('#')[1]) for line in input.split('\n')]
    position = (0, 0)
    positions = []
    j = 0
    perimeter = 0
    for instruction in instructions:
        distance = int(instruction[1])
        positions.append(position)
        perimeter += distance
        if instruction[0] == 'U':
            position = (position[0] - distance, position[1])
        elif instruction[0] == 'D':
            position = (position[0] + distance, position[1])
        elif instruction[0] == 'L':
            position = (position[0], position[1] - distance)
        elif instruction[0] == 'R':
            position = (position[0], position[1] + distance)
    positions.append(position)
    
    # using shoelace and pick's theorem
    for i, position in enumerate(positions):
        x = positions[i][0]
        last_y = positions[i-1][1]
        next_y = positions[(i+1) % len(positions)][1]
        total += x * (last_y - next_y)
    area = abs(total) / 2
    i = area - perimeter // 2 + 1
    print(area, perimeter, i)
    
    
    return int(i + perimeter)

